import unittest
from .test_hex_00_ff import TestHex00ff


def suite():
    """Test list."""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestHex00ff("test_success"),
            TestHex00ff("test_negative_number"),
            TestHex00ff("test_greater"),
            TestHex00ff("test_float"),
            TestHex00ff("test_non_number"),
            TestHex00ff("test_maximum_number"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
