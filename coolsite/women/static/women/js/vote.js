$(document).ready(function(){
  $('#like').click(function(){

        console.log('upload button clicked!')
        var fd = new FormData();
        var test = document.getElementById("like");
        var numbers = test.match(/\d{2}/g);
        test = test.replace(/\d+$/, Number.parseInt(numbers[0], 10)+1)
        console.log(test);
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