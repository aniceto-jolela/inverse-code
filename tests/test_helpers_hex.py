import unittest
from .test_helpers_hex_0_ff import TestHelpersHex


def suite():
    """@NOTE:"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestHelpersHex("test_all"),
            TestHelpersHex("test_control_characters_0_01"),
            TestHelpersHex("test_printable_characters_20_7f"),
            TestHelpersHex("test_extended_ascii_80_ff"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
