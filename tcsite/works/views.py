from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.conf import settings

from .models import Work, Media, WorksMetaTags

@cache_page(settings.CACHE_EXP_TIME)
def works(request, sorting=None):
    metas = WorksMetaTags.objects.first()
    media = Media.objects.first()
    works = Work.objects.all()
    previews = []
    for work in works:
        previews.append({'id':work.id,'name':work.name, 'url':work.preview_image.url, 'slogan':work.slogan, 'tags':work.tags.split(',')})

    tag=request.GET.get('tag')
    context = {
        'previews':previews,
        'ctag':tag,
        'media':media,

        'works_title':metas.title,
        'works_keywords':metas.keywords,
        'works_description':metas.description
    }
    return render(request,'works/works.html', context)

@cache_page(settings.CACHE_EXP_TIME)
def work(request, name):
    works = Work.objects.all()
    w = works.get(id = int(name))
    random_works = works.order_by('?')[:4]
    sh = w.screenshot_set.all()
    tags = w.tags.split(',')
    return render(request, 'works/work.html',
                  {
                      'w_id':name,
                      'work':w,
                      'screenshots':sh,
                      'w_tags':tags,
                      'random_works':random_works,
                  })