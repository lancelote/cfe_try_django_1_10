from django.db import models

from shortener.utils import generate_code


class KirrURL(models.Model):

    url       = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_shortcode(size=6):
        """Generate unique shortcode.
        """
        collisions = 0
        while collisions < 3:
            shortcode = generate_code(size=size)
            if KirrURL.objects.filter(shortcode=shortcode).exists():
                collisions += 1
            else:
                return shortcode
        raise ValueError("Can't generate unique shortcode!")

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = self.generate_shortcode()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
