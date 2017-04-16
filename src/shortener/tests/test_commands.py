from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO

from shortener.models import KirrURL


class RefreshCodesTest(TestCase):
    def setUp(self):
        for _ in range(2):
            KirrURL.objects.create()

    def test_command_output(self):
        out = StringIO()
        call_command('refreshcodes', stdout=out)
        self.assertIn('Shortcodes: 2 updated, 0 failed\n', out.getvalue())
