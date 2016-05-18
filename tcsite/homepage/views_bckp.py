from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

from tcsite.cache_utils import invalidate_template_fragment, clear_blog_cache

from .models import CarouselObj, TopVideo

@never_cache
def homepage(request):

    if 'showvideo' in request.COOKIES:
        showvideo = request.COOKIES['showvideo']
    else:
        showvideo = 'on'

    if showvideo == 'on':
        video_obj=TopVideo.objects.first()
        context = {'video_obj':video_obj}
        response = HttpResponse()
        response.set_cookie('showvideo', 'off')
        template=loader.get_template('homepage/home.html')
        renderTemplate = template.render(context)
        response.write(renderTemplate)
        return response
    else:
        images = CarouselObj.objects.all()
        context = {'images':images}
        response = HttpResponse()
        response.set_cookie('showvideo', 'on')
        template=loader.get_template('homepage/home.html')
        renderTemplate = template.render(context)
        response.write(renderTemplate)
        return response
