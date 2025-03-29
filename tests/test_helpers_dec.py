import unittest
from .test_helpers_dec_0_255 import TestHelpersDec


def suite():
    """@NOTE:"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestHelpersDec("test_all"),
            TestHelpersDec("test_control_characters_0_31"),
            TestHelpersDec("test_printable_characters_32_127"),
            TestHelpersDec("test_extended_ascii_128_255"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
