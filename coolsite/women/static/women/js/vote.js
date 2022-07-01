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
              tsislo = document.getElementById("like").textContent.match(regexp)[0]
              tsislo = Number(tsislo)+1
              document.getElementById("like").innerHTML = 'like ' + tsislo
              console.log('upload success!')

          }
        });
    });
});