from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.conf import settings

from .models import Post, TopMedia, BlogMetaTags

def posts(request):
    tag = request.GET.get('tag')
    page = request.GET.get('cname')

    if not tag:
        tag = ''

    key = 'se_blog_' + page + '_' + tag
    context = cache.get(key)

    if not context:
        postsAll = Post.objects.all()
        posts=[]

        if tag:
            for post in postsAll:
                if tag in post.tags:
                    posts.append(post)
        else:
            posts = postsAll

        paginator = Paginator(posts, settings.BLOG_POSTS_PER_PAGE)

        print('numpost = ' + str(paginator.num_pages))

        try:
            posts_page = paginator.page(page)
        except PageNotAnInteger:
            posts_page = paginator.page(1)
        except EmptyPage:
            posts_page = paginator.page(paginator.num_pages)

        p_int=int(page)
        if p_int > paginator.num_pages:
            p_int=paginator.num_pages

        back_lim = p_int - 2
        while back_lim < 1:
            back_lim += 1
        back_range = range(back_lim, p_int)

        back_placeholder = False
        if back_lim > 1:
            back_placeholder = True

        front_lim = p_int + 3 + 2 - (p_int - back_lim)
        if front_lim > paginator.num_pages:
            front_lim = paginator.num_pages + 1

        front_range = range(p_int + 1, front_lim)

        iv = p_int + 1
        if iv > paginator.num_pages:
            iv = 1

        front_placeholder = False
        if front_lim < paginator.num_pages + 1:
            front_placeholder = True

        """for i in range(0,posts_page.__len__()):
            if posts_page[i].top_set.first().text:
                posts_page[i].top_set.first().text = posts_page[i].top_set.first().text[:350] + '...'
            elif posts_page[i].bottom_set.first().text:
                posts_page[i].bottom_set.first().text = posts_page[i].bottom_set.first().text[:350] + '...'"""


        top_media = TopMedia.objects.first()

        meta_tags=BlogMetaTags.objects.first()

        context =  {
            'posts':posts_page,
            'media':top_media,
            'back_range':back_range,
            'front_range':front_range,
            'cur_page':p_int,
            'front_placeholder':front_placeholder,
            'back_placeholder':back_placeholder,
            'iv':iv,
            'current_tag':tag,
            'blog_title':meta_tags.title,
            'blog_keywords':meta_tags.keywords,
            'blog_description':meta_tags.description
        }

        cache.set(key, context, settings.CACHE_MIDDLEWARE_SECONDS)

    return render(request, 'blog/posts.html', context)


def post(request, title):

    key = 'se_post_' + title
    context = cache.get(key)

    if not context:
        p = Post.objects.get(id = int(title))
        tags = p.tags.split(',')

        next_post = Post.objects.filter(id__gt=p.id).order_by('id').first()
        if next_post==None:
            next_post=Post.objects.first()

        next_title=next_post.title
        next_slogan=next_post.slogan
        next_bg = next_post.top_image.url
        next_id = next_post.id


        carousel = p.carousel_set.all()
        topset = p.top_set.all()
        bset = p.bottom_set.all()

        context = {
            'post':p,
            'top':topset,
            'bottom':bset,
            'carousel':carousel,
            'next':next_title,
            'next_id':next_id,
            'next_slogan':next_slogan,
            'next_bg':next_bg,
            'post_tags':tags
        }
        cache.set(key, context, settings.CACHE_MIDDLEWARE_SECONDS)

    return render(request,'blog/post.html', context)