$(document).ready(function() {

 $('#form_otp').on("change paste keyup keypress blur", function(e) {
   if((e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)))
   {
     $(this).val($(this).val().replace(/[^\d].+/, ""));
     return false;
   }
   var otp=$(this).val();
    $('#otp_number').text("OTP is "+otp);
    if(otp.length===4)
    {
      $('#sub').removeClass("no_click");
    }
    else{
      $('#sub').addClass("no_click");
    }
 });

});
