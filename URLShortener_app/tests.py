from django.test import TestCase
from .models import URLShortener
from .forms import URLShortenerForm,URLShortenerUpdatingForm,test

class URLShortenerTest(TestCase):
    """
    class for testing model view and form of URLShortener_app
    """

    def setUp(self):
        url_mozl ='https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing'

        self.urlshortener_too_long= URLShortener.objects.create(url=url_mozl,hash='ghh23hkjadafsdfasasdas')
        self.urlshortener_good= URLShortener.objects.create(url=url_mozl,hash='ghh23')                                           
        self.urlshortener_empty_hash= URLShortener.objects.create(url=url_mozl,hash='')
    
    # test form - too long hash for URLShortenerForm , URLShortenerUpdatingForm
    def test_form_too_long_hash(self):
        
        #URLShortenerForm
        data = {'url':self.urlshortener_too_long.url, 'hash': self.urlshortener_too_long.hash}
        form = URLShortenerForm(data=data)
        self.assertFalse(form.is_valid())

        #URLShortenerUpdatingForm
        data = {'url':self.urlshortener_too_long.url, 'hash': self.urlshortener_too_long.hash}
        form = URLShortenerUpdatingForm(data=data)
        self.assertFalse(form.is_valid())


    # test form - good inputs for URLShortenerForm , URLShortenerUpdatingForm
    def test_form_good_valus(self):
        
        #URLShortenerForm
        data = {'url':self.urlshortener_good.url, 'hash': self.urlshortener_good.hash}
        form = URLShortenerForm(data=data)
        self.assertTrue(form.is_valid())

        #URLShortenerUpdatingForm
        data = {'url':self.urlshortener_good.url, 'hash': self.urlshortener_good.hash}
        form = URLShortenerUpdatingForm(data=data)
        self.assertTrue(form.is_valid())


    # check empty hash on model save
    def test_model_empty_hash_method(self):
        
        # check empty hash
        self.assertFalse(self.urlshortener_empty_hash.hash)

        # check that make_hash model function add hash
        self.urlshortener_empty_hash.hash = URLShortener.make_hash()
        self.assertTrue(self.urlshortener_empty_hash.hash)
