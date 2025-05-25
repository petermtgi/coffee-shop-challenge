import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        # Resetting class state
        Customer._all.clear()
        Order._all.clear()

    def test_customer_name_setter_valid(self):
        c = Customer("Peter")
        self.assertEqual(c.name, "Peter")

    def test_customer_name_setter_invalid(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("A very long name that exceeds 15")

        with self.assertRaises(ValueError):
            Customer(12345)

    def test_orders_and_coffees(self):
        c = Customer("TestUser")
        coffee1 = Coffee("Mocha")
        coffee2 = Coffee("Latte")

        c.create_order(coffee1, 4.5)
        c.create_order(coffee2, 3.0)
        c.create_order(coffee1, 5.0)

        self.assertEqual(len(c.orders()), 3)
        self.assertIn(coffee1, c.coffees())
        self.assertIn(coffee2, c.coffees())
        self.assertEqual(len(c.coffees()), 2)

    def test_most_aficionado(self):
        c1 = Customer("Richie")
        c2 = Customer("Saver")

        coffee = Coffee("Americano")

        c1.create_order(coffee, 6.0)
        c1.create_order(coffee, 3.0)
        c2.create_order(coffee, 2.5)

        self.assertEqual(Customer.most_aficionado(coffee), c1)

if __name__ == '__main__':
    unittest.main()
