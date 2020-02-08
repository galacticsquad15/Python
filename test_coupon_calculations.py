import unittest
import coupon_calculations


class MyTestCase(unittest.TestCase):
    def test_under_ten_five_dollar_off_price_five_or_less(self):
        price = coupon_calculations.calculate_price(5, 5, .10)
        self.assertEqual(price, 5.95)

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
        self.assertEqual(price, 5.95)

    def test_under_ten_ten_dollar_fifteen_percent_coupon(self):
        price = coupon_calculations.calculate_price(9, 10, .15)
        self.assertEqual(price, 5.95)

    def test_under_ten_ten_dollar_twenty_percent_coupon(self):
        price = coupon_calculations.calculate_price(9, 10, .20)
        self.assertEqual(price, 5.95)

    def test_ten_through_thirty_five_dollar_ten_coupon(self):
        price = coupon_calculations.calculate_price(10, 5, .10)
        self.assertEqual(price, 12.72)

    def test_ten_through_thirty_five_dollar_fifteen_coupon(self):
        price = coupon_calculations.calculate_price(10, 5, .15)
        self.assertEqual(price, 12.455)

    def test_ten_through_thirty_five_dollar_twenty_coupon(self):
        price = coupon_calculations.calculate_price(10, 5, .20)
        self.assertEqual(price, 12.19)

    def test_ten_through_thirty_ten_dollar_ten_coupon(self):
        price = coupon_calculations.calculate_price(10, 10, .10)
        self.assertEqual(price, 7.95)

    def test_ten_through_thirty_ten_dollar_fifteen_coupon(self):
        price = coupon_calculations.calculate_price(11, 10, .15)
        self.assertEqual(price, 8.851)

    def test_ten_through_thirty_ten_dollar_twenty_coupon(self):
        price = coupon_calculations.calculate_price(29, 10, .20)
        self.assertEqual(price, 24.062)


if __name__ == '__main__':
    unittest.main()