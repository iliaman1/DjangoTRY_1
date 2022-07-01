$(document).ready(function(){
  $('#like').click(function(){

        console.log('upload button clicked!')
        var fd = new FormData();

        $.ajax({
          data: fd,
          processData: false,
          contentType: false,
          type: 'POST',
          url: document.location.href + '/like/',
          success: function(data){
              document.getElementById("like").innerHTML = document.getElementById("like").textContent.replace(/\d+$/, parseInt($('#like').attr('value'), 10)+1);
              $('#like').val(parseInt($('#like').attr('value'), 10)+1);
              console.log('upload success!')

          }
        });
    });
});