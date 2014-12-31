from django import forms
from models import Album


class AddAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'year', 'category', 'pic', 'bio')