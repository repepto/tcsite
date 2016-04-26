from django.shortcuts import render
from django.db import models

from .models import Game


def games(request):
    games = Game.objects.all()
    previews=[]
    for game in games:
        previews.append({'name':game.name, 'url':game.preview_image.url, 'slogan':game.slogan})
        print('aaaaaaaaaaaaaaaaaaa')
        print(games.get(name='sansara').promo_image)

    print(previews)
    context = {'images':previews}

    return render(request,'games/games.html', context)

def game(request, name):
    g = Game.objects.all().get(name = name)
    sh = g.screenshot_set.all()
    tags = g.tags.split(',')
    return render(request, 'games/game.html', {'game':g, 'screenshots':sh, 'tags':tags})