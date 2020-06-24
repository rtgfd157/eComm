from django import forms
from .models import URLShortener
from django.shortcuts import get_object_or_404


class URLShortenerForm(forms.ModelForm):
    """
        form for adding url and hash
    """

    class Meta:
        model = URLShortener
        fields = ('url','hash')


class URLShortenerUpdatingForm(forms.ModelForm):
    """
    class for updating model with exsisting values for updating
    """
    class Meta:
        model = URLShortener
        fields = ('url','hash')
