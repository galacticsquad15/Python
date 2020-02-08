def main():
    me = calculate_price(9, 5, .10)
    print(me)


def calculate_price(price, cash_coupon, percent_coupon):
    sales_tax = .06
    under_ten_shipping = 5.95

    if price < 10:
        if cash_coupon == 10:
            price = under_ten_shipping
        elif price <= 5 and cash_coupon == 5:
            price = under_ten_shipping
        else:
            price -= cash_coupon
            price = price - (price * percent_coupon)
            price = price + (price * sales_tax)
            price = price + under_ten_shipping

    return price


if __name__ == '__main__':
    main()
