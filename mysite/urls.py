from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import handler404

handler404 = 'modularweb.views.page_not_found_404'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('modularweb.urls')),
]
