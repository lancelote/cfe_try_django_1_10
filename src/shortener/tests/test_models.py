from django.test import TestCase
from shortener.models import KirrURL


class KirrURLTest(TestCase):

    def test_string_representation(self):
        kirr_url = KirrURL.objects.create(url='https://hello-world.com/')
        self.assertEqual(str(kirr_url), 'https://hello-world.com/')
