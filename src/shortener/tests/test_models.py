from unittest import mock

from django.test import TestCase
from django.utils import timezone
from shortener.models import KirrURL


class KirrURLTest(TestCase):

    def test_string_representation(self):
        kirr_url = KirrURL.objects.create(url='https://hello-world.com/')
        self.assertEqual(str(kirr_url), 'https://hello-world.com/')

    def test_timestamp_is_auto_generated(self):
        create_time = timezone.now()
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = create_time
            kirr_url = KirrURL.objects.create()
        self.assertEqual(kirr_url.timestamp, create_time)

    def test_updated_is_auto_generated(self):
        create_time = timezone.now()
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = create_time
            kirr_url = KirrURL.objects.create()

            self.assertEqual(kirr_url.updated, create_time)

            update_time = create_time + timezone.timedelta(days=1)
            mock_now.return_value = update_time
            kirr_url.save()

            self.assertEqual(kirr_url.updated, update_time)
            self.assertEqual(kirr_url.timestamp, create_time)

    def test_shortcode_is_auto_generated(self):
        kirr_url = KirrURL.objects.create(url='https://hello_world.com/')
        self.assertTrue(kirr_url.shortcode)

    def test_shortcode_is_not_overwritten_on_each_save(self):
        kirr_url = KirrURL.objects.create(url='https://hello_world.com/')
        old_shortcode = kirr_url.shortcode
        kirr_url.save()
        self.assertEqual(kirr_url.shortcode, old_shortcode)
