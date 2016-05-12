from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.works, name='works'),
    url(r'^(?P<name>.+)/$', views.work, name='work'),
]