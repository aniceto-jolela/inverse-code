import unittest
from inverse_code.helpers import helpers


class TestHelpersAllAsciiTable(unittest.TestCase):
    """Test Lists all ascii table"""

    def test_all(self):
        """lists all ascii table."""
        self.assertTrue(helpers.all_ascii_table(), {})


if __name__ == "__main__":
    unittest.main()
