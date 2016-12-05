from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.conf import settings

from .models import About, AboutMetaTags

@cache_page(settings.CACHE_EXP_TIME)
def about(request):

    a = About.objects.first()
    members = a.member_set.all()
    reviews = a.review_set.all()
    brands = a.brand_set.all()
    services = a.service_set.all()

    meta_tags = AboutMetaTags.objects.first()

    return render(request,'about/about.html',{
        'about':a,
        'members':members,
        'reviews':reviews,
        'brands':brands,
        'services':services,
        'ab_title':meta_tags.title,
        'ab_keywords': meta_tags.keywords,
        'ab_description': meta_tags.description
    })
