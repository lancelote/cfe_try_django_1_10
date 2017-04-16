import unittest
from unittest import mock

from shortener.utils import generate_code


class CodeGeneratorTest(unittest.TestCase):
    def test_return_random_string(self):
        with mock.patch('random.SystemRandom.choice') as mock_choice:
            mock_choice.return_value = 'a'
            self.assertEqual(generate_code(), 'aaaaaa')

    def test_length_of_code(self):
        self.assertEqual(len(generate_code(3)), 3)
        self.assertEqual(len(generate_code(5)), 5)

    def test_chars_limit(self):
        self.assertEqual(generate_code(chars='b'), 'bbbbbb')
