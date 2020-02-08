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

    def test_thirty_through_fifty_five_dollar_ten_coupon(self):
        price = coupon_calculations.calculate_price(30, 5, .10)
        self.assertEqual(price, 35.8)

    def test_thirty_through_fifty_five_dollar_fifteen_coupon(self):
        price = coupon_calculations.calculate_price(35, 5, .15)
        self.assertEqual(price, 38.98)

    def test_thirty_through_fifty_five_dollar_twenty_coupon(self):
        price = coupon_calculations.calculate_price(30, 5, .20)
        self.assertEqual(price, 33.15)

    def test_thirty_through_fifty_ten_dollar_ten_coupon(self):
        price = coupon_calculations.calculate_price(30, 10, .10)
        self.assertEqual(price, 31.03)

    def test_thirty_through_fifty_ten_dollar_fifteen_coupon(self):
        price = coupon_calculations.calculate_price(30, 10, .15)
        self.assertEqual(price, 29.97)

    def test_thirty_through_fifty_ten_dollar_twenty_coupon(self):
        price = coupon_calculations.calculate_price(49, 10, .20)
        self.assertEqual(price, 45.022)


if __name__ == '__main__':
    unittest.main()