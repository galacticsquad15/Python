import unittest
import coupon_calculations from store


class MyTestCase(unittest.TestCase):
    def test_five_dollar_ten_percent_coupon(self):
        price = calculate_price(10, 5, .10)
        self.assertEqual(price, )


if __name__ == '__main__':
    unittest.main()