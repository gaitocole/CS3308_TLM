#!/usr/bin/python3

import unittest
from unittest import mock
import Testing.phone_number_test as phone_number_test

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

#Beginning the tests for Phonenumber Entry

    def test_digits(self):
        numblist = "1234567890"
        text = "abcdefg"
        p = phone_number_test.only_digits(numblist)
        q = phone_number_test.only_digits(text)
        self.assertTrue(p, "Numbers did not pass.")
        self.assertFalse(q, "Characters were passed into the func without issue.")

    def test_numb_of_digits(self):
        numblist_short = "123456789"
        numblist_long = "12345678910"
        numblist_justright = "0123456789"
        self.assertTrue(phone_number_test.correct_length(numblist_justright), "10 digit list didn't pass")
        self.assertFalse(phone_number_test.correct_length(numblist_long), "Greater than 10 digit list passed")
        self.assertFalse(phone_number_test.correct_length(numblist_short), "Less than 10 digit list didn't pass")

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()

