from .models import AllTags

def tags(request):
    try:
        tags = AllTags.objects.first()
        return {'tags':tags.tags.split(',')}
    except:
        return {'tags':['android', 'ios', 'flash']}
