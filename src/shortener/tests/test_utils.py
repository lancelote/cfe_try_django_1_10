import unittest
from unittest import mock

from shortener.utils import code_generator


class CodeGeneratorTest(unittest.TestCase):

    def test_return_random_string(self):
        with mock.patch('random.choice') as mock_choice:
            mock_choice.return_value = 'a'
            self.assertEqual(code_generator(), 'aaaaaa')

    def test_length_of_code(self):
        self.assertEqual(len(code_generator(3)), 3)
        self.assertEqual(len(code_generator(5)), 5)

    def test_chars_limit(self):
        self.assertEqual(code_generator(chars='b'), 'bbbbbb')
