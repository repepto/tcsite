(function($){

    $.fn.extend({
        sendPopup: function ()
        {
            return this.each(function()
            {
                var top = $(document).scrollTop();
                var left = ($(this).parent().width() - $(this).outerWidth()) / 2;
                $(this).css
                ({
                    position: 'absolute',
                    margin: 0,
                    top: top + 'px',
                    left: (left > 0 ? left : 0) + 'px',
                    opacity:0,
                    display:'block'
                });

                $(this).animate({ opacity:1 }, 700, function () {
                     $(this).delay(2000).animate({ opacity:0 }, 700, function () {
                         $(this).css({display:'none'})
                     });
                });
            });
        }
    });

	$(document).ready(function() {

		$('#contact-form').find('input,textarea').jqBootstrapValidation({
			preventSubmit: true,
            submitError: function($form, event, errors) {
				// additional error messages or events
			},
			submitSuccess: function($form, event) {
				event.preventDefault();

				var submit          = $('#contact-form submit');
				var ajaxResponse    = $('#contact-response');

				var name            = $("input#name").val();
				var email           = $("input#email").val();
				var message         = $("textarea#message").val();

				$.ajax({
					type: 'POST',
					url: '/contacts/send',
					dataType: 'json',
					data: {
						name: name,
						email: email,
						message: message,
					},
					
					beforeSend: function(result) {
						submit.empty();
						submit.append('<i class="fa fa-cog fa-spin"></i> Wait...');
					},
					success: function(result) {
						if(result.sendstatus == 1) {
							ajaxResponse.html(result.message);
							$form.fadeOut(500);
                            $('#sendResult').sendPopup();
						} else {
							ajaxResponse.html(result.message);
						}
					}
				});
			}
		});

	});

})(jQuery);


