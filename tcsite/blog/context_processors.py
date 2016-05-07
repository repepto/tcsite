from .models import AllTags

def tags(request):
    try:
        tags = AllTags.objects.first()
        return {'blog_tags':tags.tags.split(',')}
    except:
        return {'tags':['стрижка', 'маникюр', 'педикюр']}
