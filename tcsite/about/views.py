from django.shortcuts import render

from .models import About


def about(request):

    a = About.objects.all()[0]
    members = a.member_set.all()
    reviews = a.review_set.all()
    brands = a.brand_set.all()
    print('=============================================')
    print(reviews)

    return render(request,'about/about.html',{'about':a, 'members':members, 'reviews':reviews, 'brands':brands})