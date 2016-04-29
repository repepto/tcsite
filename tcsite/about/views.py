from django.shortcuts import render
from django.db import models

#from .models import About


def about(request):
    return render(request,'about/about.html')