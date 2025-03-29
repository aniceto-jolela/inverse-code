import unittest
from inverse_code.ascii.win1252 import Win1252, Hex


class TestHex00ff(unittest.TestCase):
    """Test Hexadecimal number"""

    def test_success(self):
        """Return success"""
        self.assertEqual(Win1252.hex_00_ff(self), list(Hex().code(197)))

    def test_negative_number(self):
        """return permitted values are higher than 0."""
        self.assertListEqual(list(Hex().code(-743)), [])

    def test_greater(self):
        """Return success"""
        self.assertGreater(Win1252.hex_00_ff(self), list(Hex().code(98)))

    def test_float(self):
        """
        [0 to 197] diff [197.6]\n
        return list index out of range
        """
        with self.assertRaises(IndexError):
            self.assertEqual(Win1252.hex_00_ff(self), list(Hex().code(197.3)))

    def test_non_number(self):
        """@NOTE: Expect a TypeError for non-numeric inputs"""
        with self.assertRaises(TypeError):
            list(Hex().code("197"))


if __name__ == "__main__":
    unittest.main()
