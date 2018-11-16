(function() {
  /*var video=document.getElementById('video'),
  canvas = document.getElementById('canvas'),
  context=canvas.getContext('2d'),
  photo=document.getElementById('photo_id'),
  vendorUrl=window.URL || window.webkitURL;
  navigator.getMedia = ( navigator.getUserMedia ||
                       navigator.webkitGetUserMedia ||
                       navigator.mediaDevices.getUserMedia ||
                       navigator.msGetUserMedia);
  navigator.getMedia({
    audio: false,
  video: true
  }, function(stream)
  {
    video.src =vendorUrl.createObjectURL(stream);
    video.play();
  },
  function(error)
  {

  });*/

  document.getElementById('capture_button').addEventListener('click',function(){
    /*context.drawImage(video,0,0,400,400);
    photo.setAttribute('src',canvas.toDataURL('image/png'));

    var dataURL=photo.getElementById('photo_id').value;*/
            $.ajax({
          url: "/carddetails/validate_user/",
          type:'get',
          data: {
            csrfmiddlewaretoken: window.CSRF_TOKEN
          },

          dataType: 'json',
          success: function (data) {
            console.log(data.is_taken);

          }
        });
          });
})();
