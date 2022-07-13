$(function ($) {
    $('#login_ajax').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: this.serialize(),
            dataType: 'json',
            success: function (response) {
                console.log(response)
            },
            error: function (response) {
                console.log(response)
            }
        })
    })
})