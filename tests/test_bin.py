import unittest
from .test_bin_0_1 import TestBin01


def suite():
    suite_ = unittest.TestSuite()
    suite_.addTests([TestBin01("test_success")])
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
