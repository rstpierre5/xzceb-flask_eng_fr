import unittest
from translator import *

class TestFrenchToEnglish(unittest.TestCase): 
    def testNull(self): 
        self.assertEqual(french_to_english(""), "")
    
    def testBonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        

class TestEnglishToFrench(unittest.TestCase): 
    def testNull(self): 
        self.assertEqual(english_to_french(""), "") 
    
    def testHello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        
unittest.main()