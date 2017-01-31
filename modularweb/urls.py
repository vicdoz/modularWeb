from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index),
        url('index', views.index),
        url('aboutus',views.about),
        url('contact', views.contact),
        url('gallery', views.gallery),
        url('content_page_01', views.content_page_01)
    ]