from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, TopMedia

def posts(request):

    tag = request.GET.get('tag')
    postsAll = Post.objects.all()

    posts=[]

    if tag:
        for post in postsAll:
            if tag in post.tags:
                posts.append(post)
    else:
        posts = postsAll

    paginator = Paginator(posts, 3)

    page = request.GET.get('cname')

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

    for i in range(0,posts_page.__len__()):
        if(posts_page[i].block1):
            posts_page[i].block1=posts_page[i].block1[:350] + '...'
        else:
           posts_page[i].block2=posts_page[i].block2[:350] + '...'


    top_media = TopMedia.objects.first()

    return render(request, 'blog/posts.html',
                  {
                      'posts':posts_page,
                      'media':top_media,
                      'back_range':back_range,
                      'front_range':front_range,
                      'cur_page':p_int,
                      'front_placeholder':front_placeholder,
                      'back_placeholder':back_placeholder,
                      'iv':iv
                  })


def post(request, title):

    try:
        p = Post.objects.get(title = title)
    except:
        p = Post.objects.filter(title = title).first()

    tags = p.tags.split(',')

    next_post = Post.objects.filter(id__gt=p.id).order_by('id').first()
    if next_post==None:
        next_post=Post.objects.first()

    next_title=next_post.title
    next_slogan=next_post.slogan


    carousel = p.carousel_set.all()

    return render(request,'blog/post.html', {
        'post':p,
        'carousel':carousel,
        'next':next_title,
        'next_slogan':next_slogan,
        'tags':tags
    })