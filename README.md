# hpc.social Jobs

Welcome to the hpc.social jobs board! We use the [jobs updater](https://github.com/rseng/jobs-updater) action to
programatically post to Mastodon and Slack, and also have added automation
for receiving jobs from a form. 

 - [Post a Job](https://hpc.social/jobs/about/) or read criteria and how it works.
 - [See current jobs](https://hpc.social/jobs) on our board!
 - [Visit our Mastodon Bot](https://mast.hpc.social/@jobs)
 
## Automation

We currently have the following automation implemented:

 - [Automated Posting](https://hpc.social/jobs/about/) that is updated and validated nightly.
 - [Global Counts](scripts/count_jobs.py) to have a running total of all the jobs the board has even seen (to be added).
 - [Two workflows](.github/workflows) to post to Mastodon and the HPC Social Slack
 - Anything else you'd like to see?

