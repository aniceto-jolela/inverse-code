import unittest
from .test_convert_oct import TestConvertOctal


def suite():
    """@NOTE: return all tests"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestConvertOctal("coct_decimal"),
            TestConvertOctal("coct_hexadeciaml"),
            TestConvertOctal("coct_binary"),
            TestConvertOctal("coct_symbol"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
