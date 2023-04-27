import unittest

import translator
     

class test_english_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.english_to_french('I am a woman'), 'Je suis une femme') # test when English text is 'I am a woman'
        self.assertNotEqual(translator.english_to_french('The color is red'), 'La circule est branco') # test when English text is 'The color is red'
        
class test_french_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.french_to_english('ça va bien?'), 'Is it OK?') # test when French text is 'ça va bien?'
        self.assertNotEqual(translator.french_to_english('Je suis professeur'), 'I am a president') # test when French text is 'Je suis professeur'

unittest.main()