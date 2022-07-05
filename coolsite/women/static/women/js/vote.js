$(document).ready(function(){
    function vote_post_button(id_button){
        console.log('upload button clicked!')
        var fd = new FormData();

        $.ajax({
            data: fd,
            processData: false,
            contentType: false,
            type: 'POST',
            url: document.location.href + `/${id_button}/`,
            success: function(data)
                {
                console.log($('#like').attr('data-likes'))
                console.log($('#comment_like').val())
                document.getElementById(`${id_button}`).innerHTML = document.getElementById(`${id_button}`).textContent.replace(/\d+$/, parseInt($(`#${id_button}`).attr('value'), 10)+1);
                $(`#${id_button}`).val(parseInt($(`#${id_button}`).attr('value'), 10)+1);
                console.log('upload success!')
                }
        });
    }

    function vote_comment_button(id_button){
        console.log('upload button clicked!')
        var fd = new FormData();
        id_comment = $(`#${id_button}`).val()
        $.ajax({
            data: fd,
            processData: false,
            contentType: false,
            type: 'POST',
            url: document.location.href + `/${id_button}/` + `${id_comment}`,
            success: function(data)
                {
                 console.log( id_comment = $(`#${id_button}`).val())
                console.log('upload success!')
                }
        });
    }

    $('#like').click(function(){
      vote_post_button('like')
    });
    $('#dislike').click(function(){
      vote_post_button('dislike')
    });
    $('#comment_like').click(function(){
      vote_comment_button('comment_like')
    });
    $('#comment_dislike').click(function(){
      vote_comment_button('comment_dislike')
    });
});