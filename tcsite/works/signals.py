from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from contacts.models import SocialLinks, Contacts
from homepage.models import HomeMetaTags
from .models import Work, AllTags, WorksMetaTags, Media


@receiver(post_save, sender = Work)
@receiver(post_save, sender = Media)
@receiver(post_delete, sender = Work)
@receiver(post_save, sender = WorksMetaTags)

@receiver(post_save, sender = SocialLinks)
@receiver(post_delete, sender = SocialLinks)
@receiver(post_save, sender = Contacts)
@receiver(post_delete, sender = HomeMetaTags)
@receiver(post_save, sender = HomeMetaTags)

def clear_work_cache(sender, instance, **kwargs):
    from django.http import HttpRequest

    tags = AllTags.objects.first().tags.split(',')

    request = HttpRequest()
    request.META = {'SERVER_NAME':'m8.co.ua','SERVER_PORT':80}
    request.LANGUAGE_CODE = 'en-us'
    request.path = '/works/' + str(instance.id) + '/'
    clear_view_cache(request)
    request.path = '/works/'
    clear_view_cache(request)

    for tag in tags:
        if tag:
            request.META.update({'REQUEST_METHOD':'GET', 'QUERY_STRING': 'tag=' + tag})
            request.GET.__setitem__(key='tag', value=tag)
        clear_view_cache(request)


def clear_view_cache(fake_request):
    from django.utils.cache import get_cache_key
    from django.core.cache import cache

    try:
        cache_key = get_cache_key(fake_request)
        if cache_key :
            if cache.has_key(cache_key):
                cache.delete(cache_key)
                return (True, 'successfully invalidated')
            else:
                return (False, 'cache_key does not exist in cache')
        else:
            raise ValueError('failed to create cache_key')
    except (ValueError, Exception) as e:
        return (False, e)

@receiver(post_save, sender = AllTags)
def clear_all_caches(sender, instance, **kwargs):
    clear_work_cache(sender, instance)

    from blog.signals import clear_blog_cache
    from contacts.signals import clear_contact_cache
    from about.signals import clear_about_cache

    clear_blog_cache(sender, instance)
    clear_contact_cache(sender)
    clear_about_cache(sender)
