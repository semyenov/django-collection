from django.conf.urls import patterns, include, url
from django.contrib import admin
from music.views import *
from settings import *

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^album/([0-9]+)?/$', album_view),
    url(r'^band/([0-9]+)?/$', band_view),

    #develop
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
)
