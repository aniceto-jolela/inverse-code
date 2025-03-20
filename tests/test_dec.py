import unittest
from .test_win1252 import TestWin1252

def suite():
    suite = unittest.TestSuite()
    suite.addTests([TestWin1252("test_dec_0_31"), TestWin1252("test_dec_32_127"), TestWin1252("test_dec_128_255")])
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())