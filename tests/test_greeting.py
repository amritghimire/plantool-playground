import unittest
from playground import greet


class GreetingTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_surrounding_whitespace(self):
        self.assertEqual(greet("  Ada  "), "Hello, Ada!")

    def test_unicode(self):
        self.assertEqual(greet("अमृत"), "Hello, अमृत!")

    def test_empty_is_rejected(self):
        for name in ("", " ", "\n"):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "empty"):
                greet(name)

    def test_non_text_is_rejected(self):
        with self.assertRaises(TypeError):
            greet(None)
