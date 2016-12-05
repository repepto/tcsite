from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Post, AllTags, BlogMetaTags, TopMedia

from django.conf import settings

@receiver(post_save, sender = BlogMetaTags)
@receiver(post_save, sender = Post)
@receiver(post_delete, sender = Post)
@receiver(post_save, sender = TopMedia)
@receiver(post_delete, sender = TopMedia)
def clear_blog_cache(sender, instance, **kwargs):
    if AllTags.objects.first() == None:
        t = AllTags(tags='tag0,tag1')
        t.save()

    tags = AllTags.objects.first().tags.split(',')
    tags.append('')

    num_pages = int(Post.objects.count() / settings.BLOG_POSTS_PER_PAGE) + 1

    for t in tags:
        num = 1
        while num <= num_pages:
            cache.delete('se_blog_' + str(num) + '_' + t)
            num += 1

    cache.delete('se_post_' + str(instance.id))

@receiver(post_save, sender = AllTags)
def clear_all_caches(sender, instance, **kwargs):
    clear_blog_cache(sender, instance)

    from works.signals import clear_work_cache
    from contacts.signals import clear_contact_cache
    from about.signals import clear_about_cache

    clear_work_cache(sender, instance)
    clear_contact_cache(sender)
    clear_about_cache(sender)
