import  datetime
from .models import Contacts

def tags(request):
    c = Contacts.objects.first()
    return {
        'footer_adress':c.map_adress, 'footer_phone':c.phone, 'footer_email':c.email, 'footer_year':datetime.datetime.now().year
    }
