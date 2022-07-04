$(document).ready(function(){
  function vote_button(id_button, id_comment){
      console.log('upload button clicked!')
      id_comment = id_comment || undefined
      var fd = new FormData();

      if (id_comment) {
          $.ajax({
              data: fd,
              processData: false,
              contentType: false,
              type: 'POST',
              url: document.location.href + `/${id_button}/`,
              success: function(data)
                  {
                  console.log($('#like').innerHTML)
                  document.getElementById(`${id_button}`).innerHTML = document.getElementById(`${id_button}`).textContent.replace(/\d+$/, parseInt($(`#${id_button}`).attr('value'), 10)+1);
                  $(`#${id_button}`).val(parseInt($(`#${id_button}`).attr('value'), 10)+1);
                  console.log('upload success!')
                  }
                });
      } else {


       $.ajax({
          data: fd,
          processData: false,
          contentType: false,
          type: 'POST',
          url: document.location.href + `/${id_button}/`,
          success: function(data)
              {
              console.log($('#like').attr('data-likes'))
              document.getElementById(`${id_button}`).innerHTML = document.getElementById(`${id_button}`).textContent.replace(/\d+$/, parseInt($(`#${id_button}`).attr('value'), 10)+1);
              $(`#${id_button}`).val(parseInt($(`#${id_button}`).attr('value'), 10)+1);
              console.log('upload success!')
              }
        });
      }
  }
  $('#like').click(function(){
      vote_button('like')
  });
  $('#dislike').click(function(){
      vote_button('dislike')
  });
});