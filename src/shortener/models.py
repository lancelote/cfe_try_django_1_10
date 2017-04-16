import logging

from django.db import models

from shortener.utils import generate_code

logger = logging.getLogger(__name__)


class KirrURLManager(models.Manager):
    def refresh_shortcodes(self):
        """Refresh shortcudes for all urls."""
        kirr_urls = KirrURL.objects.all()
        new, failed = 0, 0
        for kirr_url in kirr_urls:
            try:
                kirr_url.shortcode = KirrURL.generate_shortcode()
            except ValueError:
                failed += 1
            else:
                kirr_url.save()
                new += 1
        results = 'Shortcodes: {} updated, {} failed'.format(new, failed)
        logger.info(results)
        return results


class KirrURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = KirrURLManager()

    @staticmethod
    def generate_shortcode(size=6):
        """Generate unique shortcode."""
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
            try:
                self.shortcode = self.generate_shortcode()
            except ValueError as error:
                logger.exception(error)
                return
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
