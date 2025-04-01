import unittest
from inverse_code.helpers import binshow


class TestHelpersBin(unittest.TestCase):
    """Test Helpers Binary 0000 to 1111"""

    def test_control_characters_0_1(self):
        """[0 to 11111]"""
        self.assertEqual(
            binshow.control_characters_0_11111(),
            [x["bin"] for x in binshow.Bin().code(32)],
        )

    def test_printable_characters_0_1(self):
        """[0000 to 1111]"""
        self.assertEqual(
            binshow.printable_characters_100000_01111111(),
            [x["bin"] for x in binshow.Bin().code(128) if x["int"] > 32],
        )

    def test_extended_ascii_0_1(self):
        """[0000 to 1111]"""
        self.assertEqual(
            binshow.extended_ascii_10000000_11111111(),
            [x["bin"] for x in binshow.Bin().code(256) if x["int"] > 128],
        )

    def test_all(self):
        """lists all binary numbers."""
        self.assertEqual(
            binshow.all_binary(), [x["bin"] for x in binshow.Bin().code(256)]
        )


if __name__ == "__main__":
    unittest.main()
