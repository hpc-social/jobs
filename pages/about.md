---
layout: page
title: "About the hpc.social Jobs"
permalink: /about/
---

We aspire to provide a job board that is easy to search and contribute to! Criteria for your job should generally be something related to high performance computing, whether that is a linux administrator, an application developer, or a user-support specialist. You can use your best judgment. Any jobs reported by a community member to not be within this scope will be put up for discussion to the larger community and removed if deemed not in scope. To add a job,
you can either <a href="https://github.com/hpc-social/jobs" target="_blank">open a pull request</a> to directly
add a new addition to the `_data/jobs.yaml` file, or <a href="https://forms.gle/JQVsr3sVzsWhmtvz5" target="_blank">fill out our form</a>. The form is also provided here for convenience. Submissions are validated nightly, and links checked for spam or otherwise malicious content. If you don&#x27;t see your job appear the next day, please open an issue <a href="https://github.com/hpc-social/jobs/issues" target="_blank">here</a>. You can also retrieve the latest jobs via any of these feeds:

<a type="button" class="btn btn-sm btn-secondary" href="{{ site.baseurl }}/feed.json">feed.json</a>
<a type="button" class="btn btn-sm btn-secondary" href="{{ site.baseurl }}/atom.xml">atom.xml</a>

<form action="https://docs.google.com/forms/d/e/1FAIpQLSf0VwPBEtFBGpjbnBvWThesf0EoyY6Q49mapb_Q2WePD1RL5A/formResponse"
      target="_self"
      id="bootstrapForm"
      method="POST">
    <fieldset>
    <br><br><h1>Submit A Job</h1>
    </fieldset>

    <!-- Field type: "short" id: "1884453297" -->
    <fieldset>
      <legend for="1884453297">Title</legend>
      <div class="form-group">
       <p class="help-block">E.g., &quot;Linux Administrator&quot; or &quot;Applications Developer&quot;</p>
       <input id="1455288362" type="text" name="entry.1455288362" class="form-control" required>
       </div>
    </fieldset>


    <!-- Field type: "short" id: "553784508" -->
    <fieldset>
      <legend for="553784508">Employer</legend>
      <div class="form-group">
      <p class="help-block">The name of your company, institution, or group.</p>
      <input id="832560531" type="text" name="entry.832560531" class="form-control" required>
      </div>
    </fieldset>

    <!-- Field type: "short" id: "474388794" -->
    <fieldset>
    <legend for="474388794">Link to Posting</legend>
    <div class="form-group">
      <p class="help-block">Please provide a link to the primary job posting or description.</p>
      <input id="1066279785" type="text" name="entry.1066279785" class="form-control" required>
      </div>
    </fieldset>

    <!-- Field type: "short" id: "1167938019" -->
    <fieldset>
    <legend for="1167938019">Location</legend>
    <div class="form-group">
     <p class="help-block">E.g., &quot;Boulder, CO&quot; or &quot;Remote&quot;</p>
      <input id="1467472745" type="text" name="entry.1467472745" class="form-control" required>
     </div>
    </fieldset>

    <!-- Field type: "choices" id: "790761790" -->
    <fieldset>
     <legend for="790761790">Job Type</legend>
     <div class="form-group">
     <div class="radio">
    <label><input type="radio" name="entry.547613891" value="Full-Time" required>Full-Time</label></div>
    <div class="radio"><label>
    <input type="radio" name="entry.547613891" value="Part-Time" required>Part-Time</label></div>
    <div class="radio">
    <label><input type="radio" name="entry.547613891" value="Consulting" required>Consulting</label></div>
    <div class="radio"><label><input type="radio" name="entry.547613891" value="Internship" required>Internship</label></div>
   <div class="radio"><label><input type="radio" name="entry.547613891" value="Volunteer" required>Volunteer</label></div></div>
    </fieldset>

    <!-- Field type: "choices" id: "1643825093" -->
    <fieldset>
    <legend for="1643825093">Remote Status</legend>
    <div class="form-group">
    <div class="radio">
    <label>
    <input type="radio" name="entry.1933684676" value="Fully onsite" required>
    Fully onsite
    </label>
    </div>
    <div class="radio">
    <label>
    <input type="radio" name="entry.1933684676" value="Remote friendly" required>
    Remote friendly
    </label>
    </div>
    <div class="radio">
    <label>
    <input type="radio" name="entry.1933684676" value="Hybrid" required>
    Hybrid
    </label>
    </div>
    <div class="radio">
    <label>
    <input type="radio" name="entry.1933684676" value="Fully remote" required>
    Fully remote
    </label>
    </div>
   </div>
    </fieldset>


    <!-- Field type: "date" id: "83288553" -->
    <fieldset>
<legend for="83288553">Expires</legend>
<div class="form-group">
    <p class="help-block">When does this posting expire (e.g., should no longer appear on the board? We recommend a few months from the posted date).</p>
    <input type="date" id="1751423871_date" placeholder="1/6/2023" class="form-control" required>
</div>
    </fieldset>

    <input type="hidden" name="fvv" value="1">
    <input type="hidden" name="fbzx" value="-6475620142414990367">
    <!--
CAVEAT: In multipages (multisection) forms, *pageHistory* field tells to google what sections we've currently completed.
This usually starts as "0" for the first page, then "0,1" in the second page... up to "0,1,2..N" in n-th page.
Keep this in mind if you plan to change this code to recreate any sort of multipage-feature in your exported form.
We're setting this to the total number of pages in this form because we're sending all fields from all the section together.
    -->
    <input type="hidden" name="pageHistory" value="0">

    <input class="btn btn-primary" type="submit" value="Submit">
</form>
