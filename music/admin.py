from django.contrib import admin
from music.models import *

admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Track)