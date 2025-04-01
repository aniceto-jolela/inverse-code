import unittest
from .test_helpers_bin_0_1 import TestHelpersBin


def suite():
    """@NOTE:"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestHelpersBin("test_all"),
            TestHelpersBin("test_control_characters_0_1"),
            TestHelpersBin("test_printable_characters_0_1"),
            TestHelpersBin("test_extended_ascii_0_1"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
