import unittest
from inverse_code import encode


class TestEncode(unittest.TestCase):
    """List test"""

    def test_encode(self):
        """success"""
        self.assertEqual(encode.encode("FRED"), 251792692)

    def test_single_character(self):
        """return decimal number"""
        self.assertEqual(encode.encode("A"), 16777217)

    def test_non_alphanumerics(self):
        """return decimal number"""
        self.assertEqual(encode.encode(" :^)"), 79094888)

    def test_raw_characters(self):
        """return decimal number"""
        self.assertEqual(encode.encode("foo"), 124807030)

    def test_raw_characters2(self):
        """return decimal number"""
        self.assertEqual(encode.encode(" foo"), 250662636)

    def test_raw_characters3(self):
        """return decimal number"""
        self.assertEqual(encode.encode("foot"), 267939702)

    def test_raw_characters4(self):
        """return decimal number"""
        self.assertEqual(encode.encode("BIRD"), 251930706)

    def test_raw_characters5(self):
        """return decimal number"""
        self.assertEqual(encode.encode("...."), 15794160)

    def test_raw_characters6(self):
        """return decimal number"""
        self.assertEqual(encode.encode("^^^^"), 252706800)

    def test_raw_characters7(self):
        """return decimal number"""
        self.assertEqual(encode.encode("Woot"), 266956663)

    def test_raw_characters8(self):
        """return decimal number"""
        self.assertEqual(encode.encode("no"), 53490482)

    def test_raw_characters10(self):
        """return can only be in maximum 4 characters."""
        with self.assertRaises(ValueError):
            encode.encode("Aniceto")


if __name__ == "__main__":
    unittest.main()
