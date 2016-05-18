from django.db.models.signals import post_save
from django.dispatch import receiver

from works.signals import clear_view_cache

from .models import About, AboutMetaTags

@receiver(post_save, sender = About)
@receiver(post_save, sender = AboutMetaTags)
def clear_about_cache(sender, **kwargs):
    from django.http import HttpRequest

    request = HttpRequest()
    request.META = {'SERVER_NAME':'127.0.0.1','SERVER_PORT':8000}
    request.LANGUAGE_CODE = 'en-us'
    request.path = '/about/'
    clear_view_cache(request)