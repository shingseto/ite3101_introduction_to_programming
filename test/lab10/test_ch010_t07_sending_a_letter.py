import unittest
from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import execfile

if is_answer:
    from lab10.ch010_t07_sending_a_letter_ans import *
else:
    from lab10.ch010_t07_sending_a_letter import *


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual("A", get_letter_grade(90))
        self.assertEqual("B", get_letter_grade(80))
        self.assertEqual("C", get_letter_grade(70))
        self.assertEqual("D", get_letter_grade(60))
        self.assertEqual("F", get_letter_grade(50))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab10/ch010_t07_sending_a_letter.py", globals())

        expected = """B
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
