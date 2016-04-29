from django.shortcuts import render
from django.db import models

from .models import Game


def getPreviews():
    games = Game.objects.all()
    previews = []
    for game in games:
        previews.append({'name':game.name, 'url':game.preview_image.url, 'slogan':game.slogan, 'tags':game.tags.split(',')})

    print("___________________________")
    print(previews)
    return previews


def games(request):
    context = {'previews':getPreviews()}

    return render(request,'games/games.html', context)

def game(request, name):
    if name[0] == '_':
        context = {'previews':getPreviews(), 'ctag':name[1:]}
        return render(request,'games/games.html', context)
    else:
        g = Game.objects.all().get(name = name)
        sh = g.screenshot_set.all()
        tags = g.tags.split(',')
        return render(request, 'games/game.html', {'game':g, 'screenshots':sh, 'tags':tags})