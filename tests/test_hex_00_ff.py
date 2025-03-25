import unittest
from inverse_code.ascii.win1252 import Win1252, Hex


class TestHex00ff(unittest.TestCase):
    """Test Decimal number"""

    def test_success(self):
        """Return success"""
        self.assertDictEqual(Win1252.hex_00_FF(self), list(Hex().code(109)))

    def test_greater(self):
        """Return success"""
        self.assertEqual(Win1252.hex_00_FF(self), list(Hex().code(288)))


if __name__ == "__main__":
    unittest.main()
