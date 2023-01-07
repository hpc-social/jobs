//Initialize table for jobs
$('.jobs-table').DataTable( {
     order: [[ 1, "asc" ]], //set date column as default order, earliest to latest
     lengthMenu: [ 20, 50, 100 ], //options for entry control
     dom: '<"search-wrap"f<"dropfilters">><"top" l<"clear">><"bottom" tipl>', //https://datatables.net/examples/basic_init/dom.html
     language: {
      emptyTable:     "There are no jobs available at this time",
      search: "Search by keyword",
      zeroRecords: "No jobs match your search criteria. Try again or clear the search to start over.",
      info: "Showing _START_ to _END_ • _TOTAL_",
      lengthMenu:     "Show _MENU_ jobs",
    }    
} );


$(document).ready(function() {
  var dropfilters = $("#filter-wrapper").html();
  var placement = document.querySelector(".dropfilters");
  $(placement).append(dropfilters);
  
  var cleartoggle = $("#clear").html();
  var placementb = document.querySelector(".clear");
  $(placementb).append(cleartoggle);

  // Hide second length picker
  $($('.dataTables_length')[1]).hide()

  $( "#min" ).datepicker({
      dateFormat: "mm/dd/yy",
      showAnim: 'slideDown',
      showButtonPanel: true ,
      autoSize: true,
      currentText: "Clear"
  });

  $('#min').bind('keyup','keydown', function(event) {
  var inputLength = event.target.value.length;
  if (event.keyCode != 8){
    if(inputLength === 2 || inputLength === 5){
      var thisVal = event.target.value;
      thisVal += '/';
      $(event.target).val(thisVal);
     }
    }
  })

  $('.timepicker').timepicker({hourMin: 7, hourMax: 13,
    timeFormat: "hh:mm tt",
    showAnim: 'slideDown',
    buttonText: "Select time",
    currentText: "Clear",
    controlType: 'select',
    oneLine: true,
    stepMinute: 30,
    defaultValue: "07:00 am" //select the first option
  });

    $("#timeCustom").click(function(){
        $(".ui-datepicker-current").addClass("clear-time-only");
        $(".ui-datepicker-current").removeClass("clear-date-only");
    });
  $("#min").click(function(){
        $(".ui-datepicker-current").removeClass("clear-time-only");
    $(".ui-datepicker-current").addClass("clear-date-only");
    });

    $('.timepicker').bind('keyup','keydown', function(event) {
    var inputLength = event.target.value.length;
    if (event.keyCode != 9){
      if(inputLength === 2){
        var thisVal = event.target.value;
        thisVal += ':';
        $(event.target).val(thisVal);
      }
      if (inputLength === 5){
        var spaceVal = event.target.value;
        spaceVal += ' ';
        $(event.target).val(spaceVal);
      }
    }
  })
});





$(document).ready(function() {
   var table =  $('.jobs-table').DataTable();
    
    // Jobs type is in row 1, locations in 2
    $('#job-type-filter').on('change', function () {
      table.columns(1).search(this.value).draw();
    });
    $('#location-filter').on('change', function () {
      table.columns(3).search( this.value ).draw();
    });
    $('#remote-filter').on('change', function () {
      table.columns(6).search( this.value ).draw();
    });
    $('#employer-filter').on('change', function () {
      table.columns(2).search( this.value ).draw();
    });
  
    $('.timepicker').on( 'keyup change input', function () {
      var v =$(this).val();  // getting search input value
      table.columns(5).search(v).draw();
    });

    // Posted after (min)
    $('#min').on('change', function () {
       var from = $(this).val().replace(/\//g, ''); //remove the slashes
       var num = 4;
       var result = from.substr(num) + from.substr(0, num);
       $.fn.dataTable.ext.search.push(
         function(settings, data, dataIndex) {           
           return $(table.row(dataIndex).node()).attr('data-posted') >= result;
       });
       table.draw();
    });


    // Expires before
    $('#timeCustom').on('change', function () {
       var from = $(this).val().replace(/\//g, ''); //remove the slashes
       var num = 4;
       var result = from.substr(num) + from.substr(0, num);
       $.fn.dataTable.ext.search.push(
         function(settings, data, dataIndex) {           
           return $(table.row(dataIndex).node()).attr('data-posted') <= result;
       });
       table.draw();
    });
});


//Clear all fields in the search
$(document).ready(function() {
  var table =  $('.jobs-table').DataTable();
$('#clear-all').click(function() {
    $('#DataTables_Table_0_filter input, .form-control').val("");
    table.search('').draw(); //required after
    table.columns(0).search("").draw();
    table.columns(1).search("").draw();
    table.columns(2).search("").draw();
    table.columns(3).search("").draw();
    table.columns(4).search("").draw();
    $.fn.dataTable.ext.search.pop();
    table.draw();
       
});
});

// Add background colors to filters that are not empty
$(document).ready(function() {
  $('#DataTables_Table_0_filter input, .form-control').on('keyup change input', 
   function(){
     var field = $( this );        
    if ( field.val() != '' ) {
        field.addClass('data-entered');
    } else {
        field.removeClass('data-entered');
    }
});
 $('#clear-all').on('click', 
   function(){
   $('#DataTables_Table_0_filter input, .form-control').removeClass('data-entered');
 });
 
});

// Set clear on the datpicker clear button
$(document).on("click", ".clear-date-only", function(){ // if they click clear
  var table =  $('.jobs-table').DataTable();
  var inputs =  $('#DataTables_Table_0_filter input, .form-control');
    $('#min').val("");
    $.fn.dataTable.ext.search.pop();
    table.draw();
    inputs.removeClass('data-entered');
});

// Set clear on the timepicker button
$(document).on("click", ".clear-time-only", function(){ // if they click clear
   var table =  $('.jobs-table').DataTable();
    var inputs =  $('#DataTables_Table_0_filter input, .form-control');
    $('.timepicker').val("");
    $('.ui-timepicker-select').val("");
    table.columns(2).search("").draw();
    inputs.removeClass('data-entered');
});
