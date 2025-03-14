#!/usr/bin/env python3

import unittest

from pizza_price import order_price

class TestOrderPrice(unittest.TestCase):

    def test_typical_order_not_tuesday_no_delivery(self):
        self.assertEqual(order_price(10, 2, False, False), 20)

    def test_typical_order_not_tuesday_with_delivery(self):
        self.assertEqual(order_price(10, 2, False, False), 22.5)

if __name__ == '__main__':
    unittest.main()
