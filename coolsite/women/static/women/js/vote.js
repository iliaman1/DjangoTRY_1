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
              const regexp = /\d+$/
              document.getElementById("like").innerHTML = 'likes '+ Number(document.getElementById("like").textContent.match(regexp)[0])+Number(1)
              console.log('upload success!')

          }
        });
    });
});