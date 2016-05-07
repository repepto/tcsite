from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

from .models import CarouselObj, TopVideo

#showvideo = True

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
        requestContext=RequestContext(request, context)
        template=loader.get_template('homepage/home.html')
        renderTemplate = template.render(requestContext)
        response.write(renderTemplate)
        return response
    else:
        images = CarouselObj.objects.all()
        context = {'images':images}
        response = HttpResponse()
        response.set_cookie('showvideo', 'on')
        requestContext=RequestContext(request, context)
        template=loader.get_template('homepage/home.html')
        renderTemplate = template.render(requestContext)
        response.write(renderTemplate)
        return response
