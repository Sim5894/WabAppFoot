$('form input:checkbox').change(function() {
   id = $(this).attr('id')
   if($(this).is(":checked")) {
        $("#titu"+id).prop('disabled', false);
        $("#but"+id).prop('disabled', false);
        $("#jaune"+id).prop('disabled', false);
        $("#rouge"+id).prop('disabled', false);
   }
   if($(this).prop("checked") == false){
        $("#titu"+id).prop('disabled', true);
        $("#but"+id).prop('disabled', true);
        $("#jaune"+id).prop('disabled', true);
        $("#rouge"+id).prop('disabled', true);
   }
});