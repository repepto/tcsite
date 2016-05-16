from .models import AllTags

def tags(request):
    try:
        tags = AllTags.objects.first().tags
        return {'blog_tags':tags.split(',')}
    except:
        return {'tags':[]}
