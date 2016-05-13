from .models import AllTags

def tags(request):
    try:
        tags = AllTags.objects.first()
        return {'blog_tags':tags.split(',')}
    except:
        return {'tags':[]}
