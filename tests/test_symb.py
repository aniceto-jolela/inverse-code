import unittest
from .test_ascii.test_sybol_32_127 import TestSymbol


def suite():
    """Test list."""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestSymbol("test_success"),
            TestSymbol("test_non_number"),
            TestSymbol("test_maximum_number"),
        ]
    )
    return suite_


if __name__ == "__mani__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
