import unittest
from inverse_code.ascii.win1252 import Win1252, Bin


class TestBin01(unittest.TestCase):
    """Test Binary number"""

    def test_success(self):
        """return success"""
        self.assertEqual(Win1252.bin_01(self), list(Bin().code(256)))

    def test_negative_number(self):
        """return permitted values are higher than 0."""
        with self.assertRaises(ValueError):
            self.assertListEqual(list(Bin().code(-743)), [])

    def test_float(self):
        """[256] equal [255.1]"""
        self.assertEqual(Win1252.bin_01(self), list(Bin().code(255.1)))

    def test_non_number(self):
        """@NOTE: Expect a TypeError for non-numeric inputs"""
        with self.assertRaises(TypeError):
            list(Bin().code("256"))

    def test_maximum_number(self):
        """@NOTE: The maximum number of this list is 256"""
        with self.assertRaises(ValueError):
            self.assertEqual(Win1252.bin_01(self), list(Bin().code(257)))


if __name__ == "__main__":
    unittest.main()
