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
    alert($(this).serialize());
    $.ajax({
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        data: $(this).serialize(),
        success: function (data) {
            alert(data);
        },
        error: function(data) {
            alert('Something went wrong!');
        }
    });
    return false;
});