import datetime
from .models import Contacts, SocialLinks, MetaTags

def tags(request):
    c = Contacts.objects.first()
    links = SocialLinks.objects.first()
    metaTags = MetaTags.objects.first()
    return {
        'footer_adress':c.map_adress,
        'footer_phone':c.phone,
        'footer_email':c.email,
        'footer_year':datetime.datetime.now().year,

        'facebook_href':links.facebook,
        'twitter_href':links.twitter,
        'instagram_href':links.instagram,
        'behance_href':links.behance,
        'dribble_href':links.dribble,

        'meta_title':metaTags.title,
        'meta_keywords':metaTags.keywords,
        'meta_description':metaTags.description,
    }
