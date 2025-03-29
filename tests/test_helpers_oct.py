import unittest
from .test_helpers_oct_0_377 import TestHelpersOct


def suite():
    """@NOTE:"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestHelpersOct("test_all"),
            TestHelpersOct("test_control_characters_0_37"),
            TestHelpersOct("test_printable_characters_40_177"),
            TestHelpersOct("test_extended_ascii_200_377"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
