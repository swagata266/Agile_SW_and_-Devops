# test_my_program.py

import unittest
import my_program

class TestMyProgram(unittest.TestCase):

    def test_add_numbers(self):
        result = my_program.add_numbers(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()