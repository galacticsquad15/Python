import unittest
import camper_age_input

    
class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_convert_to_months(self):
        numberOfMonths = camper_age_input.convert_to_months(3)
        self.assertEqual(36, numberOfMonths)


if __name__ == '__main__':
    unittest.main()
