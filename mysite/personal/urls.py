from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#since the url is "^$", the url is fed no arguments (home page, default page, whatever you wanna call it)
    url(r'^contact/$', views.contact, name='contact'),
]
