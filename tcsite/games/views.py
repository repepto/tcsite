from django.shortcuts import render
from django.db import models

from .models import Game, Media



def games(request):
    media = Media.objects.all()[0]
    games = Game.objects.all()
    previews = []
    for game in games:
        previews.append({'name':game.name, 'url':game.preview_image.url, 'slogan':game.slogan, 'tags':game.tags.split(',')})

    tag=request.GET.get('tag')
    context = {'previews':previews, 'ctag':tag, 'media':media}

    return render(request,'games/games.html', context)

def game(request, name):
        games = Game.objects.all()
        g = games.get(name = name)
        random_works = games.order_by('?')[:4]
        sh = g.screenshot_set.all()
        tags = g.tags.split(',')
        return render(request, 'games/game.html', {'game':g, 'screenshots':sh, 'g_tags':tags, 'random_works':random_works})