import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []  # Reset orders
        self.alice = Customer("Alice")
        self.latte = Coffee("Latte")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("A" * 16)  # Too long
        with self.assertRaises(ValueError):
            Customer(123)  # Wrong type

    def test_orders(self):
        order = self.alice.create_order(self.latte, 5.0)
        self.assertEqual(self.alice.orders(), [order])

    def test_coffees(self):
        self.alice.create_order(self.latte, 5.0)
        self.assertEqual(self.alice.coffees(), [self.latte])

    def test_most_aficionado(self):
        bob = Customer("Bob")
        self.alice.create_order(self.latte, 5.0)
        bob.create_order(self.latte, 6.0)
        self.assertEqual(Customer.most_aficionado(self.latte), bob)

if __name__ == "__main__":
    unittest.main()