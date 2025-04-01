import unittest
from inverse_code.helpers import decshow


class TestHelpersDec(unittest.TestCase):
    """Test Helpers Decimal 0 to 255"""

    def test_control_characters_0_31(self):
        """[0 to 31]"""
        self.assertEqual(decshow.control_characters_0_31(), list(range(32)))

    def test_printable_characters_32_127(self):
        """[32 to 127]"""
        self.assertEqual(decshow.printable_characters_32_127(), list(range(32, 128)))

    def test_extended_ascii_128_255(self):
        """[128 to 255]"""
        self.assertEqual(decshow.extended_ascii_128_255(), list(range(128, 256)))

    def test_all(self):
        """lists all decimal numbers."""
        self.assertCountEqual(decshow.all_decimal(), list(range(256)))


if __name__ == "__main__":
    unittest.main()
