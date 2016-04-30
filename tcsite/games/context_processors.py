from .models import AllTags, TopImage

def tags(request):
    try:
        tags = AllTags.objects.all()[0]
        return {'tags':tags.tags.split(',')}
    except:
        return {'tags':['android', 'ios', 'flash']}


def game_top_img(request):
    try:
        game_top_img = TopImage.objects.all()[0]
        return {'game_top_img':game_top_img.image.url}
    except:
        return None
