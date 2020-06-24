from django import forms
from .models import URLShortener
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError


def test(val):
    non_url_safe = ['"', '#', '$', '%', '&', '+',
                    ',', '/', ':', ';', '=', '?',
                    '@', '[', '\\', ']', '^', '`',
                    '{', '|', '}', '~', "'"]

    non_safe = [c for c in val if c in non_url_safe]
    if non_safe:
        raise ValidationError("Hash shouldn't be using : {}".format(non_url_safe))


class URLShortenerForm(forms.ModelForm):
    """
        form for adding url and hash
    """

    hash = forms.CharField( max_length = 15  ,required=False ,validators=[test]  )

    class Meta:
        model = URLShortener
        fields = ('url','hash')


class URLShortenerUpdatingForm(forms.ModelForm):
    """
    class for updating model with exsisting values for updating
    """
    hash = forms.CharField( max_length = 15  ,required=False ,validators=[test]  )

    class Meta:
        model = URLShortener
        fields = ('url','hash')
