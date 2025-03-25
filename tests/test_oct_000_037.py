import unittest
from inverse_code.ascii.win1252 import Win1252, Oct


class TestDec0377(unittest.TestCase):
    """Test Decimal number"""

    def test_success(self):
        """Return success"""
        self.assertEqual(Win1252.oct_000_377(self), list(Oct().code(378)))


if __name__ == "__main__":
    unittest.main()
