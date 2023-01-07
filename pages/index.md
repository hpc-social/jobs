---
layout: default
permalink: /
---

{% assign jobs = site.data.jobs | sort: "posted" | reverse %}
{% assign job_types = site.data.jobs | map: 'job_type' | uniq %}
{% assign locations = site.data.jobs | map: 'location' | uniq %}
{% assign remote_types = site.data.jobs | map: 'remote' | uniq %}
{% assign employer_types = site.data.jobs | map: 'employer' | uniq %}

<div class="container my-4">
  <div class="row">
    <div class="col-sm-12">
      <div id="camp-search">
      <template id="clear">
      <div class="reset-filter-toggle">
      <button title="Refresh Search" id="clear-all">Clear search</button>
      </div>
      </template>
      <template id="filter-wrapper">
      <div class="row">
      <div class="col-md-4 col-6 arrow-down">
       <label>Job Type</label> 
       <select id="job-type-filter" class="form-control">
       <option></option>
       {% for job_type in job_types %}<option>{{ job_type }}</option>{% endfor %}
       </select>
       </div> 
       <div class="col-md-4 col-6 arrow-down">
       <label>Location</label>
       <select id="location-filter" class="form-control">
       <option></option>
       {% for location in locations %}<option>{{ location }}</option>{% endfor %}
       </select>
       </div>
       <div class="col-md-4 col-6 arrow-down">
       <label>Employer</label>
       <select id="employer-filter" class="form-control">
       <option></option>
       {% for employer in employer_types %}<option>{{ employer }}</option>{% endfor %}
       </select>
       </div>
        
       <div class="col-6 date-wrapper">
       <label>Posted after</label>
       <input type="text" id="min" class="datepicker form-control" placeholder="mm/dd/yyyy">
       <em class="help">Show jobs that were posted on (and after) selected date</em>
       </div>
       <div class="col-6">
       <label>Remote Options</label>
       <select id="remote-filter" class="form-control">
       <option></option>
       {% for remote_type in remote_types %}<option>{{ remote_type }}</option>{% endfor %}
       </select>
       </div>

      </div>
      </template>

<table class="jobs-table mt-4 table table-responsive">
  <thead>
    <tr>
      <th data-sortable="true" width="30%">Name</th>
      <th data-sortable="true" data-field="job-type" width="15%">Job Type</th>
      <th data-sortable="true" data-field="location" width="15%">Employer</th>
      <th data-sortable="true" data-field="location" width="15%">Location</th>
      <th data-sortable="true" data-field="expires">Expires</th>
      <th data-sortable="true" data-field="posted" width="10%">Posted</th>
      <th data-sortable="true" data-field="remote" width="10%">Remote Options</th>
   </tr>
  </thead>
  <tbody>
    {% include jobrows.html sorted_jobs=jobs %}
  </tbody>
    </table>
    </div>
    </div>
</div>
</div>
