import unittest
from .test_convert.test_convert_symb import TestConvertSymbol


def suite():
    """@NOTE: return all tests"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestConvertSymbol("csymb_decimal"),
            TestConvertSymbol("csymb_octal"),
            TestConvertSymbol("csymb_hexadecimal"),
            TestConvertSymbol("csymb_binary"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
