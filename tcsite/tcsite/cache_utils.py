from django.core.cache.utils import make_template_fragment_key
from django.core.cache import cache
from blog.models import AllTags

def invalidate_template_fragment(fragment_name, *variables):
    cache_key = make_template_fragment_key(
        fragment_name, vary_on=variables)
    cache.delete(cache_key)
    print('---------------------------')
    print(cache_key)

def clear_blog_cache():

    tags = AllTags.objects.first().tags.split(',')
    tags.append('')

    for t in tags:
        num = 1
        while cache.get('blog_' + str(num) + '_' + t):
            cache.delete('blog_' + str(num) + '_' + t)