from django import forms
from .models import UrlShort


class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model = UrlShort
        fields = ('original_url',)

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'})
        }
