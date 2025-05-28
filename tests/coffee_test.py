import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []  # Reset orders
        self.latte = Coffee("Latte")
        self.alice = Customer("Alice")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("ab")  # Too short
        with self.assertRaises(ValueError):
            Coffee(123)  # Wrong type
        with self.assertRaises(AttributeError):
            self.latte.name = "Mocha"  # Immutable

    def test_orders(self):
        order = Order(self.alice, self.latte, 5.0)
        self.assertEqual(self.latte.orders(), [order])

    def test_customers(self):
        Order(self.alice, self.latte, 5.0)
        self.assertEqual(self.latte.customers(), [self.alice])

    def test_num_orders(self):
        Order(self.alice, self.latte, 5.0)
        self.assertEqual(self.latte.num_orders(), 1)

    def test_average_price(self):
        Order(self.alice, self.latte, 5.0)
        Order(self.alice, self.latte, 7.0)
        self.assertEqual(self.latte.average_price(), 6.0)

if __name__ == "__main__":
    unittest.main()