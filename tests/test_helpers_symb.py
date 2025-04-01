import unittest
from .test_helpers_symb_32_127 import TestHelpersSymb


def suite():
    """@NOTE:"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestHelpersSymb("test_all"),
            TestHelpersSymb("test_printable_characters_32_127"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
