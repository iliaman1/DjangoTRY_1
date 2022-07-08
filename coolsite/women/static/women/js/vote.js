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
        }
    }


    class PostVote extends Vote{
        like(post_slug){
            if(this.process(`/${post_slug}/like`)===true){
                document.getElementById(`like`).innerHTML = document.getElementById(`like`).textContent.replace(/\d+$/, parseInt($(`#like`).attr('value'), 10)+1);
                $(`#like`).val(parseInt($(`#like`).attr('value'), 10)+1);
                console.log('upload success!')
            }
        }

        dislike(post_slug){
            if(this.process(`/${post_slug}/dislike`)===true){
                document.getElementById(`dislike`).innerHTML = document.getElementById(`dislike`).textContent.replace(/\d+$/, parseInt($(`#dislike`).attr('value'), 10)-1);
                $(`#dislike`).val(parseInt($(`#dislike`).attr('value'), 10)-1);
                console.log('upload success!')
            }
        }
    }
});