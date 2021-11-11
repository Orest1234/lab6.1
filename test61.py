import unittest
import atp61 as code


class TestProgramm(unittest.TestCase):

    def test_create(self):
        low = -20
        high = 34
        size = 20
        a_list = code.create(low, high, size)
        b_list = []
        for number in a_list:
            if number <= high or number >= low:
                b_list.append(number)
            else:
                pass

        self.assertEqual(a_list, b_list)



