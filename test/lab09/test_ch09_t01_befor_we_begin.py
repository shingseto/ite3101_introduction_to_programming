# ch09_t01_befor_we_begin
import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab09/ch09_t01_befor_we_begin.py")

        expected = """Adam
Alex
Mariah
Martine
Columbus
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
