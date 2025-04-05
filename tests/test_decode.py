import unittest
from inverse_code import decode


class TestDecode(unittest.TestCase):
    """List test"""

    def test_decode(self):
        """success"""
        self.assertEqual(decode.decode(251792692), "FRED")

    def test_single_character(self):
        """return A"""
        self.assertEqual(decode.decode(16777217), "A")

    def test_non_alphanumerics(self):
        """return [ :^)]"""
        self.assertEqual(decode.decode(79094888), " :^)")

    def test_raw_characters(self):
        """return foo"""
        self.assertEqual(decode.decode(124807030), "foo")

    def test_raw_characters2(self):
        """return [ foo]"""
        self.assertEqual(decode.decode(250662636), " foo")

    def test_raw_characters3(self):
        """return decimal number"""
        self.assertEqual(decode.decode(267939702), "foot")

    def test_raw_characters4(self):
        """return BIRD"""
        self.assertEqual(decode.decode(251930706), "BIRD")

    def test_raw_characters5(self):
        """return [...]"""
        self.assertEqual(decode.decode(15794160), "....")

    def test_raw_characters6(self):
        """return [^^^^]"""
        self.assertEqual(decode.decode(252706800), "^^^^")

    def test_raw_characters7(self):
        """return Woot"""
        self.assertEqual(decode.decode(266956663), "Woot")

    def test_raw_characters8(self):
        """return [no]"""
        self.assertEqual(decode.decode(53490482), "no")

    def test_raw_characters10(self):
        """return can only be in maximum 9 characters."""
        with self.assertRaises(ValueError):
            decode.decode(9856447203845687093)


if __name__ == "__main__":
    unittest.main()
