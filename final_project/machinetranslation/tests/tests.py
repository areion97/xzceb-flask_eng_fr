import unittest
import json
from translator import Translator

class TestStringMethods(unittest.TestCase):
    def test_positive(self):
        firstValue = "Salut"
        message = "Not correct"
        y = Translator.english_to_french(self,"Hi")['translations'][0]['translation']
        self.assertEqual(firstValue,y, message)
    
    def test_positive2(self):
        firstValue = "Hi"
        message = "Not correct"
        y = Translator.french_to_english(self,"Salut")['translations'][0]['translation']
        self.assertEqual(firstValue,y, message)
  
if __name__ == '__main__':
    unittest.main()
