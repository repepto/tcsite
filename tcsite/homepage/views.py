from django.shortcuts import render

from .models import CarouselObj


def homepage(request):
    images = CarouselObj.objects.all()
    context = {'images':images}
    #print(context['images'][0].image.url)
    return render(request,'homepage/home.html', context)