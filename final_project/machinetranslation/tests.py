import unittest
from translator import english_To_French, french_To_English

class TestMyModule(unittest.TestCase):

    def test_english_To_French(self):
        self.assertNotEqual(english_To_French("Null"), "")
    def test_english_To_French2(self):
        self.assertEqual(english_To_French('Hello'), 'Bonjour')

    def test_french_To_English(self):
        self.assertNotEqual(french_To_English("Null"), "")
    def test_french_To_English2(self):
        self.assertEqual(french_To_English('Bonjour'), 'Hello')

if __name__=='__main__':
    unittest.main()
