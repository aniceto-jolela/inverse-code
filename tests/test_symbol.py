import unittest
from .test_sybol_32_127 import TestSymbol


def suite():
    suite_ = unittest.TestSuite()
    suite_.addTests([TestSymbol("test_success")])
    return suite_


if __name__ == "__mani__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
