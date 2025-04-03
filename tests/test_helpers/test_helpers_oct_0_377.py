import unittest
from inverse_code.helpers import octshow


class TestHelpersOct(unittest.TestCase):
    """Test Helpers Oct 0 to 377"""

    def test_control_characters_0_37(self):
        """[0 to 37]"""
        self.assertEqual(
            octshow.control_characters_0_37(),
            [x["oct"] for x in octshow.Oct().code(38)],
        )

    def test_printable_characters_40_177(self):
        """[40 to 177]"""
        self.assertEqual(
            octshow.printable_characters_40_177(),
            [x["oct"] for x in octshow.Oct().code(178, 40)],
        )

    def test_extended_ascii_200_377(self):
        """[200 to 377]"""
        self.assertEqual(
            octshow.extended_ascii_200_377(),
            [x["oct"] for x in octshow.Oct().code(378, 200)],
        )

    def test_all(self):
        """lists all octal numbers."""
        self.assertEqual(
            octshow.all_octal(), [x["oct"] for x in octshow.Oct().code(378)]
        )


if __name__ == "__main__":
    unittest.main()
