$(document).ready(function(){
    class Vote{
        process(url){
            $.ajax({
                data: new FormData(),
                processData: false,
                contentType: false,
                type: 'POST',
                url: url,
                success: function (data){
                    return true
                }
            })

            return false
        }
    }


    class PostVote extends Vote{
        like(){
            if(this.process(document.location.href + '/like/') === true){
                console.log('upload success!')
            }
        }

        dislike(){
            if(this.process(document.location.href + '/dislike/') === true){
                console.log('upload success!')
            }
        }
    }


    class CommentVote extends Vote{
        like(commen_id){
            if(this.process(document.location.href + `/comment_like/${commen_id}`) === true){

            }
        }

        dislike(commen_id){
            if(this.process(document.location.href + `/comment_dislike/${commen_id}`) === true){

            }
        }
    }


    let postvote = new PostVote();
    $('#like').click(function(){
         $(this)[0].innerHTML = $(this)[0].innerHTML.replace(/\d+$/, parseInt($(`#like`).attr('value'), 10)+1);
         $(`#like`).val(parseInt($(`#like`).attr('value'), 10)+1);
        postvote.like()
    })
    $('#dislike').click(function(){
        $(this)[0].innerHTML = $(this)[0].innerHTML.replace(/\d+$/, parseInt($(`#dislike`).attr('value'), 10)+1);
        $(`#dislike`).val(parseInt($(`#dislike`).attr('value'), 10)+1);
        postvote.dislike()
    })

    let commentvote = new CommentVote();
    $('.comment_like').click(function(){
        let id_comment = this.value
        $(this)[0].innerHTML = $(this)[0].innerHTML.replace(/\d+$/, parseInt($(this).attr('data-likes'), 10)+1)
        $(this).attr('data-likes', parseInt($(this).attr('data-likes'),10)+1)
        commentvote.like(id_comment)

    })
    $('.comment_dislike').click(function(){
        let id_comment = this.value
        $(this)[0].innerHTML = $(this)[0].innerHTML.replace(/\d+$/, parseInt($(this).attr('data-dislikes'), 10)+1)
        $(this).attr('data-dislikes', parseInt($(this).attr('data-dislikes'),10)+1)
        commentvote.dislike(id_comment)
    })
});