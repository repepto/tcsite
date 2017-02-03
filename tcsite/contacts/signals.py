from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from works.signals import clear_view_cache

from .models import Contacts, SocialLinks
from homepage.models import HomeMetaTags

@receiver(post_save, sender = Contacts)
@receiver(post_save, sender = HomeMetaTags)
@receiver(post_save, sender = SocialLinks)
@receiver(post_delete, sender = SocialLinks)
def clear_contact_cache(sender, **kwargs):
    from django.http import HttpRequest

    request = HttpRequest()
    request.META = {'SERVER_NAME':'m8.co.ua','SERVER_PORT':80}
    request.LANGUAGE_CODE = 'en-us'
    request.path = '/contacts/'
    clear_view_cache(request)

    invalidate_template_fragment('template_footer')

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

def invalidate_template_fragment(fragment_name, *variables):
    cache_key = make_template_fragment_key(
        fragment_name, vary_on=variables) 
    cache.delete(cache_key)