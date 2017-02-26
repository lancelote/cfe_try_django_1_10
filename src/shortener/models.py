from django.db import models

from shortener.utils import code_generator


class KirrURL(models.Model):

    url       = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True)
    updated   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
