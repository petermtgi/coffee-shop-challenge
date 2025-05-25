import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Customer._all.clear()
        Coffee._all.clear()
        Order._all.clear()

    def test_order_valid_init(self):
        c = Customer("Lena")
        coffee = Coffee("Macchiato")
        order = Order(c, coffee, 5.0)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_order_invalid_customer(self):
        coffee = Coffee("Cortado")
        with self.assertRaises(TypeError):
            Order("NotACustomer", coffee, 3.5)

    def test_order_invalid_coffee(self):
        c = Customer("Mark")
        with self.assertRaises(TypeError):
            Order(c, "NotACoffee", 3.5)

    def test_order_invalid_price(self):
        c = Customer("Leo")
        coffee = Coffee("Brew")

        with self.assertRaises(ValueError):
            Order(c, coffee, 0.99)  # Too cheap

        with self.assertRaises(ValueError):
            Order(c, coffee, 12.0)  # Too expensive

        with self.assertRaises(ValueError):
            Order(c, coffee, "NotAFloat")  # Wrong type

if __name__ == '__main__':
    unittest.main()
