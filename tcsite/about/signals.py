from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache.utils import make_template_fragment_key

from .models import About

@receiver(post_save, sender = About)
def clear_blog_cache(sender, instance, **kwargs):
    key = make_template_fragment_key('se_template_about')
    cache.delete(key)