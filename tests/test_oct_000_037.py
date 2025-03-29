import unittest
from inverse_code.ascii.win1252 import Win1252, Oct


class TestOct0377(unittest.TestCase):
    """Test Octal number"""

    def test_success(self):
        """return success"""
        self.assertEqual(Win1252.oct_000_377(self), list(Oct().code(378)))

    def test_negative_number(self):
        """return permitted values are higher than 0."""
        with self.assertRaises(ValueError):
            self.assertListEqual(list(Oct().code(-156)), [])

    def test_greater(self):
        """return 378 > 200"""
        self.assertGreater(Win1252.oct_000_377(self), list(Oct().code(200)))

    def test_float(self):
        """[0 to 378] equal [378.97]"""
        self.assertEqual(Win1252.oct_000_377(self), list(Oct().code(378.97)))

    def test_non_number(self):
        """@NOTE: Expect a TypeError for non-numeric inputs"""
        with self.assertRaises(TypeError):
            list(Oct().code("378"))


if __name__ == "__main__":
    unittest.main()
