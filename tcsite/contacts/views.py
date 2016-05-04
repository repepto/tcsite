import json

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

from .models import Contacts


def contacts(request):

    contact = Contacts.objects.all()[0]
    return render(request, 'contacts/contacts.html', {'contact':contact})

def send(request):
    send_mail('Site message', request.POST.get('cmessage'), request.POST.get('cemail'),
              ['tabletcrushers@gmail.com'], fail_silently=False);

    data = {'aaaa':'111'}

    dataj=json.dumps(data)

    return HttpResponse(dataj, content_type='application/json')
