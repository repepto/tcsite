(function($){
    $.fn.extend({
        center: function ()
        {
            return this.each(function()
            {
                var top = $(document).scrollTop() - 56;
                var left = ($(this).parent().width() - $(this).outerWidth()) / 2;
                $(this).css
                ({
                    position: 'absolute',
                    margin: 0,
                    top: top + 'px',
                    left: (left > 0 ? left : 0) + 'px'
                });

                $(this).animate({ top: top + 56 }, 4700);
            });
        }
    });
})(jQuery);

$(window).load(function() {
    $('#sendResult').center();
});

$('#contact-form').submit(function () {
    alert('aaaaaa1234567');
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
        success: function (data) {
            $("#SOME-DIV").html(data);
            alert('aaaaaaaaaaaaa');
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
            alert('aaaaaaaaaaaaa');
        }
    });
    return false;
});