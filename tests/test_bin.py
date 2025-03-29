import unittest
from .test_bin_0_1 import TestBin01


def suite():
    """Test list."""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestBin01("test_success"),
            TestBin01("test_negative_number"),
            TestBin01("test_float"),
            TestBin01("test_non_number"),
            TestBin01("test_maximum_number"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
