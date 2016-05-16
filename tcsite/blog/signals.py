from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Post
from .models import AllTags

from django.conf import settings


@receiver(post_save, sender = Post)
@receiver(post_delete, sender = Post)
def clear_blog_cache(sender, instance, **kwargs):
    tags = AllTags.objects.first().tags.split(',')
    tags.append('')

    num_pages = int(Post.objects.count() / settings.BLOG_POSTS_PER_PAGE)
    print('NUM PAGES = ' + str(num_pages))

    for t in tags:
        num = 1
        print('num = ' + str(num_pages))
        while num <= num_pages:
            cache.delete('se_blog_' + str(num) + '_' + t)
            print('se_blog_' + str(num) + '_' + t)
            num += 1

    cache.delete('se_post_' + str(instance.id))