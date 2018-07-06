import types
import unittest
from test.unit_test_helper.console_test_helper import *
from unit_test_helper import is_answer

if is_answer:
    from lab07.ch07_t03_getting_there_ans import plane_ride_cost
else:
    from lab07.ch07_t03_getting_there import plane_ride_cost


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab07/ch07_t03_getting_there.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['plane_ride_cost'], types.FunctionType)
        self.assertEqual(183, plane_ride_cost("Charlotte"))
        self.assertEqual(220, plane_ride_cost("Tampa"))
        self.assertEqual(222, plane_ride_cost("Pittsburgh"))
        self.assertEqual(475, plane_ride_cost("Los Angeles"))
        self.assertEqual(None, plane_ride_cost(""))


if __name__ == '__main__':
    unittest.main()
