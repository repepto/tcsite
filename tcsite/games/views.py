from django.shortcuts import render

from .models import Game


def games(request):
    games = Game.objects.all()
    previews=[]
    for game in games:
        previews.append(game.preview_image.url)
    for game in games:
        previews.append(game.preview_image.url)
    for game in games:
        previews.append(game.preview_image.url)
    for game in games:
        previews.append(game.preview_image.url)
    print(previews)
    context = {'images':previews}

    return render(request,'games/games.html', context)