import unittest
import coupon_calculations


class MyTestCase(unittest.TestCase):
    def test_under_ten_five_dollar_ten_percent_coupon(self):
        price = coupon_calculations.calculate_price(9, 5, .10)
        self.assertEqual(price, 9.766)

    def test_under_ten_five_dollar_fifteen_percent_coupon(self):
        price = coupon_calculations.calculate_price(9, 5, .15)
        self.assertEqual(price, 9.554)

    def test_under_ten_five_dollar_twenty_percent_coupon(self):
        price = coupon_calculations.calculate_price(9, 5, .20)
        self.assertEqual(price, 9.342)

    def test_under_ten_ten_dollar_ten_percent_coupon(self):
        price = coupon_calculations.calculate_price(9, 10, .10)
        self.assertEqual(price, 0)

    def test_under_ten_ten_dollar_fifteen_percent_coupon(self):
        price = coupon_calculations.calculate_price(9, 10, .15)
        self.assertEqual(price, 0)

    def test_under_ten_ten_dollar_twenty_percent_coupon(self):
        price = coupon_calculations.calculate_price(9, 10, .20)
        self.assertEqual(price, 0)


if __name__ == '__main__':
    unittest.main()