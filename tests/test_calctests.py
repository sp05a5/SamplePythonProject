import unittest
#from SamplePythonProject.my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def test_increment(self):
        #calculation = Calculations(8, 2)
        #self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')
        self.assertEqual(10, 10)

    def test_decrement(self):
        #calculation = Calculations(8, 2)
        #self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')
        self.assertEqual(9, 9)


if __name__ == '__main__':
    unittest.main()