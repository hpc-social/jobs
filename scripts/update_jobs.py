#!/usr/bin/env python3

# Retrieve new jobs from the online form and validate
# Update with new jobs
# Also check for expiration and remove these from the site
# Copyright @vsoch, 2020-2023

import os
import datetime
from datetime import timedelta
from urlchecker.core.urlproc import UrlCheckResult
import shutil
import tempfile
import requests
import yaml
import urllib
import json
import sys

here = os.path.dirname(os.path.abspath(__file__))

scanned_url_file = os.path.join(here, "scanned-urls.txt")
scanner_token = os.environ.get("SCANNER_KEY")


def load_scanned_urls():
    """
    Load previously scanned cache of safe URLs.
    Any unsafe urls will be removed from the sheet.
    """
    scanned_urls = set()

    # Ensure we read in previously scanned URLs to not waste API quota (5k/month)
    if os.path.exists(scanned_url_file):
        with open(scanned_url_file) as fd:
            scanned_urls = set([x.strip() for x in fd.read().split("\n") if x.strip()])
    return scanned_urls


scanned_urls = load_scanned_urls()


def save_scanned_urls():
    """
    Save updated scanned urls.
    """
    global scanned_urls

    print(f"Saving updated urls to {scanned_url_file}")
    with open(scanned_url_file, "w") as fd:
        for url in scanned_urls:
            fd.write(url + "\n")


def is_malicious_url(url):
    """
    Use spam detection api to look for malicious URLs.
    """
    global scanned_urls

    # We've scanned it, and it's not malicious
    if url in scanned_urls:
        print(f"{url} has been previously seen and marked safe.")
        return False

    encoded_url = urllib.parse.quote(url, safe="")
    api_url = "https://ipqualityscore.com/api/json/url/%s/" % scanner_token
    response = requests.get(api_url + encoded_url)
    if response.status_code != 200:
        sys.exit("Issue using IP quality score API.")

    result = response.json()
    print(f"New result for {url}:")
    print(json.dumps(result, indent=4))

    # We don't allow any of this!
    if (
        result["suspicious"]
        or result["phishing"]
        or result["malware"]
        or result["spamming"]
        or result["adult"]
    ):
        print(
            "This result is not safe - determined to be suspicious, phishing, malware, spamming, or adult."
        )
        return True

    # If we get here, add to our scanned_urls
    scanned_urls.add(url)
    return False


def get_filepath(filename):
    """
    load the jobs file.
    """
    filepath = os.path.join(os.path.dirname(here), "_data", filename)

    # Exit on error if we cannot find file
    if not os.path.exists(filepath):
        print("Cannot find %s" % filepath)

    return filepath


def read_jobs(filepath):
    """
    read in the jobs data.
    """
    with open(filepath, "r") as fd:
        data = yaml.load(fd.read(), Loader=yaml.SafeLoader)
    return data


def get_google_sheet():
    """
    Read tab separated values sheet with locations!
    """
    # A tsv download for just the worksheet with city, state
    sheet = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRcy977Aq4RZ_8piW7UoTo6ktxuQKpzvH9yDFm6vEorJ77JLsVO7D0Fu3flzrg2NWL1oinRTfNyk2x4/pub?gid=1531821430&single=true&output=tsv"

    # Ensure the response is okay
    response = requests.get(sheet)
    if response.status_code != 200:
        print(
            "Error with getting sheet, response code %s: %s"
            % (response.status_code, response.reason)
        )
        sys.exit(1)

    # Split lines by all sorts of fugly carriage returns
    lines = response.text.split("\r\n")

    # Remove empty responses, header row, make all lowercase
    lines = [x.strip('"').strip() for x in lines[1:] if x.strip()]
    return lines


def parse_lines(lines):
    """
    Parse new jobs from lines
    """

    def _convert_date(srcdate:str):
      converted = datetime.datetime.strptime(srcdate, "%m/%d/%Y")
      return datetime.date.fromisoformat(converted.date().isoformat())

    jobs = []
    for line in lines:
        line = [x.strip() for x in line.split("\t")]
        posted = _convert_date(line[0].split(" ")[0].strip())
        title = line[1].replace('"', "'")
        url = line[2].strip()
        location = line[3].strip()
        job_type = line[4].strip()
        remote = line[5].strip()
        expires = _convert_date(line[6].strip())
        employer = line[7].strip()

        # If we have a url and key, check if
        if url and scanner_token:
            if is_malicious_url(url):
                sys.exit(f"Malicious url {url} detected, cancelling update.")

        jobs.append(
            {
                "posted": posted,
                "title": title,
                "url": url,
                "location": location,
                "job_type": job_type,
                "remote": remote,
                "expires": expires,
                "employer": employer,
            }
        )

    return jobs


def update_jobs(file):
    """
    clean out expired job postings from a file
    """
    filepath = get_filepath(file)
    print("jobs file is: %s" % filepath)

    # Copy a version to be previous
    previous_file = os.path.join(os.path.dirname(here), "_data", "previous-jobs.yaml")
    shutil.copyfile(filepath, previous_file)

    # Read in the jobs, add new jobs from sheets
    jobs = read_jobs(filepath)
    seen = set([f"{x['url']}-{x['title']}" for x in jobs])
    lines = get_google_sheet()
    new_jobs = parse_lines(lines)

    # Add jobs we haven't seen (based on url and title for now)
    for job in new_jobs:
        if f"{job['url']}-{job['title']}" in seen:
            continue
        jobs.append(job)

    # Keep a list to re-write to file
    keepers = []
    
    now = datetime.date.fromisoformat(datetime.date.today().isoformat())

    print("Found %s jobs" % len(jobs))
    for job in jobs:
        # Do not keep expired jobs that haven't been updated in 60 days
        if job["expires"] < now:
            removal_date = job["expires"] + timedelta(days=60)
            if removal_date < now:
                print(
                    "Skipping %s, expired and hasn't been updated in 60 days."
                    % job["title"]
                )
                continue

        # catch these and fail
        if job["expires"] > now:
            print("Keeping %s, expires in future." % job["title"])
            keepers.append(job)
            continue

        # If it's expired and we are considering keeping/removing:
        checker = UrlCheckResult()
        checker.check_urls(urls=[job["url"]], retry_count=3, timeout=5)

        # If the url passes, add to keepers
        if checker.passed:
            print("PASSED %s" % job["url"])
            keepers.append(job)
        else:
            print(
                "FAIL %s is expired and did not pass, not adding back to jobs."
                % job["url"]
            )

    # update the user
    print("%s jobs have passed." % len(keepers))

    # Finally, update data file
    _, tmpfile = tempfile.mkstemp(prefix="jobs-", suffix=".yaml")

    # Write the new file
    with open(tmpfile, "w") as outfile:
        yaml.dump(keepers, outfile, allow_unicode=True)

    # Copy finished file - will need to be added in pull request
    shutil.copyfile(tmpfile, filepath)
    save_scanned_urls()


def main():
    """
    a small helper to update the jobs posting files.
    """
    update_jobs("jobs.yaml")


if __name__ == "__main__":
    main()
