from django.db import models
from django.urls import reverse
import random
import string


class URLShortener(models.Model):
    """
    class that transform url into hash by user input or auto if empty

    """

    url =  models.URLField(max_length=200, blank=False,null=False, verbose_name='URL')
    hash = models.CharField(null=True,blank=True, max_length=15,verbose_name="Hash")

    def __str__(self):
        return  self.url + ' ' +self.hash

    # when in form there is empty hash field will return randomly hash
    def make_hash():
        ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
        STRING_LENGTH = 12
        return "".join(random.choice(ALPHANUMERIC_CHARS) for _ in range(STRING_LENGTH ))

    def get_absolute_url(self):
        return reverse('/')