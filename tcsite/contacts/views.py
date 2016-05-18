import json

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.cache import cache_page

from .models import Contacts

@cache_page(settings.CACHE_EXP_TIME)
def contacts(request):

    contact = Contacts.objects.first()
    return render(request, 'contacts/contacts.html', {'contact':contact})

def send(request):
    email = Contacts.objects.first().email
    send_mail('Site message', request.POST.get('cmessage'), request.POST.get('cemail'),
              [email], fail_silently=False);

    data = {'status':'ok'}

    dataj=json.dumps(data)

    return HttpResponse(dataj, content_type='application/json')
