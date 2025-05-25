import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Coffee._all.clear()
        Order._all.clear()
        Customer._all.clear()

    def test_valid_coffee_name(self):
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.name, "Espresso")

    def test_invalid_coffee_name(self):
        with self.assertRaises(ValueError):
            Coffee("A")  # too short

        with self.assertRaises(ValueError):
            Coffee(123)  # not a string

    def test_coffee_orders_customers(self):
        c1 = Customer("Jess")
        c2 = Customer("Sam")
        coffee = Coffee("Flat White")

        c1.create_order(coffee, 4.5)
        c2.create_order(coffee, 5.0)

        self.assertEqual(len(coffee.orders()), 2)
        self.assertIn(c1, coffee.customers())
        self.assertIn(c2, coffee.customers())

    def test_num_orders_and_average(self):
        coffee = Coffee("Latte")
        c = Customer("Chad")
        c.create_order(coffee, 4.0)
        c.create_order(coffee, 6.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(coffee.average_price(), 5.0)

        # Edge case: no orders
        new_coffee = Coffee("Cappuccino")
        self.assertEqual(new_coffee.num_orders(), 0)
        self.assertEqual(new_coffee.average_price(), 0)

if __name__ == '__main__':
    unittest.main()
