$(document).ready( function() {
	$.getJSON("/pull/block/",{ajax: 'true'}, function(j){
      var options = '';
      options += '<option value="-1">Please Choose</option>';
      for (var i = 0; i < j.length; i++) {
        options += '<option value="' + j[i].fields.block_name + '">' + j[i].fields.block_name + '</option>';
      }
      $("select#baseapp_block").html(options);
    })



$('select#block').change(function() {
$.getJSON("/pull/school/?did="+$(this).val(),{ajax: 'true'}, function(j){
      var options = '';
      options += '<option value="-1">Please Choose</option>';
      for (var i = 0; i < j.length; i++) {
        options += '<option value="' + j[i].fields.school_name + '">' + j[i].fields.school_name + '</option>';
      }
      $("select#school").html(options);
    })

});
});