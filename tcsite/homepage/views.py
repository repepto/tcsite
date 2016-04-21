from django.shortcuts import render

from .models import Carousel


def homepage(request):
    images = Carousel.objects.all()
    context = {'images':images}
    #print(context['images'][0].image.url)
    return render(request,'homepage/index.html', context)