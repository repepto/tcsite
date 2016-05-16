from .models import AllTags

def tags(request):
    try:
        tags = AllTags.objects.first().tags
        return {'tags':tags.split(',')}
    except:
        return {'tags':[]}
