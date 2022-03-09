#!/usr/bin/python3

import newPassword as t
import unittest

class newPasswordTestCase(unittest.TestCase):

    def test_reqChars_Pass(self):
        self.assertTrue(t.reqChars("testing1"), "Input contains both a digit and a letter, should return True.")

    def test_reqChars_NoLetters(self):
        self.assertFalse(t.reqChars("11111111"), "Input contains only digits, should return False.")
        
    def test_reqChars_NoNumbers(self):
        self.assertFalse(t.reqChars("testingg"), "Input contains only letters, should return False.")
        
    def test_testMatch_Pass(self):
        self.assertTrue(t.testMatch("testing1", "testing1"), "Inputs identical, should return True.")
        
    def test_testMatch_Fail(self):
        self.assertFalse(t.testMatch("testing1", "testing2"), "Inputs differ, should return False.")
    
    def test_minLength_Pass(self):        
        self.assertTrue(t.minLength("testing1"), "Minimum length should be 8, input length is also 8.")
        
    def test_minLength_Fail(self):
        self.assertFalse(t.minLength("testing"), "Minimum length should be 8, but input length is only 7.")

if __name__ == '__main__':
    unittest.main()