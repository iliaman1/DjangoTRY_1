$(document).ready(function(){
  function vote_button(id_button){
      console.log('upload button clicked!')
      var fd = new FormData();

       $.ajax({
          data: fd,
          processData: false,
          contentType: false,
          type: 'POST',
          url: document.location.href + `/${id_button}/`,
          success: function(data){
              document.getElementById(`${id_button}`).innerHTML = document.getElementById(`${id_button}`).textContent.replace(/\d+$/, parseInt($(`#${id_button}`).attr('value'), 10)+1);
              $(`#${id_button}`).val(parseInt($(`#${id_button}`).attr('value'), 10)+1);
              console.log('upload success!')

          }
        });
  }
  $('#like').click(function(){
      vote_button('like')
  });
  $('#dislike').click(function(){
      vote_button('dislike')
  });
});