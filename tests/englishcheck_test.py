"""Unit tests for english language checker"""
import unittest
import libcipher.utils as utils


class EnglishChecktestCase(unittest.TestCase):
    def test_for_english(self):
        x = utils.EnglishChecker()
        self.assertTrue(x.is_english("Mary had a little lamb"))

    def test_for_non_english(self):
        x = utils.EnglishChecker()
        self.assertFalse(x.is_english("Mary avait un petit agneau"))

    def test_for_no_letters(self):
        x = utils.EnglishChecker()
        self.assertFalse(x.is_english("222 #@#!#<:"))

if __name__ == '__main__':
    unittest.main()
