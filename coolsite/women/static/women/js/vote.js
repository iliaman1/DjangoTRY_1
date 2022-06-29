$(document).ready(function(){
  $('#like').click(function(){

        console.log('upload button clicked!')
        var fd = new FormData();

        $.ajax({
          url: '/post/gestiya/like/',
          data: fd,
          processData: false,
          contentType: false,
          type: 'POST',
          success: function(data){
            console.log('upload success!')

          }
        });
    });
});