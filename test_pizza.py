#!/usr/bin/env python3

import unittest

from pizza_price import order_price

class TestOrderPrice(unittest.TestCase):

    def test_buy_one_get_one_ahlf_price_even_number(self):
        self.assertEqual(order_price(10, 2, True, False), 15)

    def test_buy_one_get_one_half_price_odd_number(self):
        self.assertEqual(order_price(10, 3, True, False), 25)

    def test_typical_order_not_tuesday_no_delivery(self):
        self.assertEqual(order_price(10, 2, False, False), 20)

    def test_typical_order_not_tuesday_no_delivery_different_price(self):
        self.assertEqual(order_price(18, 2, False, False), 36)

    def test_typical_order_not_tuesday_no_delivery_different_quantity(self):
        self.assertEqual(order_price(10, 5, False, False), 50)

    def test_typical_order_not_tuesday_with_delivery(self):
        self.assertEqual(order_price(10, 2, False, True), 22.5)

    def test_typical_order_tuesday_no_delivery(self):
        self.assertEqual(order_price(10, 2, True, False), 15)

if __name__ == '__main__':
    unittest.main()
