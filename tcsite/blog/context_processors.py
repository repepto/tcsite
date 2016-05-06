from .models import AllTags

def tags(request):
    try:
        tags = AllTags.objects.all()[0]
        return {'blog_tags':tags.tags.split(',')}
    except:
        return {'tags':['стрижка', 'маникюр', 'педикюр']}
