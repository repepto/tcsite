from django.shortcuts import render
from django.db import models

from .models import Work, Media



def works(request):
    media = Media.objects.first()
    works = Work.objects.all()
    previews = []
    for work in works:
        previews.append({'name':work.name, 'url':work.preview_image.url, 'slogan':work.slogan, 'tags':work.tags.split(',')})

    tag=request.GET.get('tag')
    context = {'previews':previews, 'ctag':tag, 'media':media}

    return render(request,'works/works.html', context)

def work(request, name):
    works = Work.objects.all()
    w = works.get(name = name)
    random_works = works.order_by('?')[:4]
    sh = w.screenshot_set.all()
    tags = w.tags.split(',')
    return render(request, 'works/work.html', {'work':w, 'screenshots':sh, 'w_tags':tags, 'random_works':random_works})