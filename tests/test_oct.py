import unittest
from .test_oct_000_037 import TestOct0377


def suite():
    """Test list."""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestOct0377("test_success"),
            TestOct0377("test_negative_number"),
            TestOct0377("test_greater"),
            TestOct0377("test_float"),
            TestOct0377("test_non_number"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
