from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
import json

from .models import Contacts


def contacts(request):
    return render(request, 'contacts/contacts.html')

def send(request):
    print ('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print ()
    send_mail('Site message', request.POST.get('cmessage'), request.POST.get('cemail'),
              ['tabletcrushers@gmail.com'], fail_silently=False);

    data = {'aaaa':'111'}

    dataj=json.dumps(data)

    return HttpResponse(dataj, content_type='application/json')
