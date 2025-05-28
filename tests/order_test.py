import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []  # Reset orders
        self.alice = Customer("Alice")
        self.latte = Coffee("Latte")

    def test_initialization(self):
        order = Order(self.alice, self.latte, 5.0)
        self.assertEqual(order.customer, self.alice)
        self.assertEqual(order.coffee, self.latte)
        self.assertEqual(order.price, 5.0)

    def test_price_validation(self):
        with self.assertRaises(ValueError):
            Order(self.alice, self.latte, 0.5)  # Too low
        with self.assertRaises(ValueError):
            Order(self.alice, self.latte, 11.0)  # Too high
        with self.assertRaises(ValueError):
            Order(self.alice, self.latte, "5.0")  # Wrong type

    def test_price_immutability(self):
        order = Order(self.alice, self.latte, 5.0)
        with self.assertRaises(AttributeError):
            order.price = 6.0

if __name__ == "__main__":
    unittest.main()