import datetime
from .models import Contacts, SocialLinks
from homepage.models import HomeMetaTags

def tags(request):
    contacts = Contacts.objects.first()
    links = SocialLinks.objects.first()
    metaTags = HomeMetaTags.objects.first()

    if contacts == None:
        contacts = Contacts(map_adress = 'adress', phone = '777', email = 'email')
        contacts.save()

    if links == None:
        links = SocialLinks(
            facebook = 'facebook_link',
            twitter='twitter_link',
            instagram='instagram_link',
            behance='behance_link',
            dribble='dribble_link'
        )

        links.save()

    if metaTags == None:
        metaTags = MetaTags(title='title',keywords='keywords0,keywords1',description='description')
        metaTags.save()

    return {
        'footer_adress':contacts.map_adress,
        'footer_phone':contacts.phone,
        'footer_email':contacts.email,
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
