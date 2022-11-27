import unittest
from ibm_watson import LanguageTranslatorV3

class TestMyModule(unittest.TestCase):

    def englishToFrench(self):
        self.assertNotEqual(englishToFrench("Null"), "")
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def frenchToEnglish(self):
        self.assertNotEqual(frenchToEnglish("Null"), "")
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
