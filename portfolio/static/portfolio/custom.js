function runScript() {
    $.ajax({
        url: 'do_something', //The URL you defined in urls.py
        success: function(data) {
          //If you wish you can do additional data manipulation here.
        }

    });
}


$(function () {
    var frm = $('#contactForm');
    frm.submit(function (ev) {
        $('#form_id').trigger("reset");
        $.ajax({
            type: frm.attr('method'),
            url: 'do_something',
            data: frm.serialize(),
            success: function (data) {
                $("#contactForm")[0].reset();
                alert('Thanks for reaching out, I will get back to you ASAP')
            }
        });
        ev.preventDefault();
    });
});
