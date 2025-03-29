import unittest
from inverse_code.ascii.win1252 import Win1252, Dec


class TestDec0255(unittest.TestCase):
    """Test Decimal number"""

    def test_success(self):
        """return success"""
        self.assertEqual(Win1252.dec_0_255(self), list(Dec().code(256)))

    def test_negative_number(self):
        """@NOTE: Permitted values are higher than 0."""
        with self.assertRaises(ValueError):
            self.assertIsNotNone(Win1252.dec_0_255(self), list(Dec().code(-256)))

    def test_greater(self):
        """return 255 > 200"""
        self.assertGreater(Win1252.dec_0_255(self), list(Dec().code(200)))

    def test_float(self):
        """[0 to 254] equal [254]"""
        self.assertEqual(Win1252.dec_0_255(self), list(Dec().code(255.97)))

    def test_non_number(self):
        """@NOTE: Expect a TypeError for non-numeric inputs"""
        with self.assertRaises(TypeError):
            list(Dec().code("255"))

    def test_maximum_number(self):
        """@NOTE: The maximum number of this list is 256"""
        with self.assertRaises(ValueError):
            self.assertEqual(Win1252.dec_0_255(self), list(Dec().code(257)))


if __name__ == "__main__":
    unittest.main()
