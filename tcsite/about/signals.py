from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from contacts.models import SocialLinks, Contacts
from homepage.models import HomeMetaTags
from works.signals import clear_view_cache

from .models import About, AboutMetaTags

@receiver(post_save, sender = About)
@receiver(post_save, sender = AboutMetaTags)
@receiver(post_save, sender = SocialLinks)
@receiver(post_delete, sender = SocialLinks)
@receiver(post_save, sender = Contacts)
@receiver(post_delete, sender = HomeMetaTags)
@receiver(post_save, sender = HomeMetaTags)

def clear_about_cache(sender, **kwargs):
    from django.http import HttpRequest

    request = HttpRequest()
    request.META = {'SERVER_NAME':'m8.co.ua','SERVER_PORT':80}
    request.LANGUAGE_CODE = 'en-us'
    request.path = '/about/'
    clear_view_cache(request)
