from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='home'),
        url('index', views.index, name='home'),
        url('home', views.index, name='home'),
        url('aboutus',views.about, name='about'),
        url('contact', views.contact, name='contact'),
        url('gallery', views.gallery, name='gallery'),
        url('content_page_01', views.content_page_01, name='content_page'),
    ]