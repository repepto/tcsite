from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache.utils import make_template_fragment_key

from .models import Work
from .models import AllTags

@receiver(post_save, sender = Work)
@receiver(post_delete, sender = Work)
def clear_blog_cache(sender, instance, **kwargs):
    tags = AllTags.objects.first().tags.split(',')
    tags.append(None)

    for t in tags:
        key = make_template_fragment_key('se_template_works', [t])
        print(key)
        cache.delete(key)

    key = make_template_fragment_key('se_template_work', [instance.id])
    cache.delete(key)