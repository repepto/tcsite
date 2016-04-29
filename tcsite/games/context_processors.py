from .models import AllTags

def tags(request):
    try:
        tags = AllTags.objects.all()[0]
        return {'tags':tags.tags.split(',')}
    except:
        return {'tags':['android', 'ios', 'flash']}