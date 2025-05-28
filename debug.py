from customer import Customer
from coffee import Coffee
from order import Order


if __name__ == "__main__":
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    # Create orders
    order1 = alice.create_order(latte, 5.0)
    order2 = alice.create_order(espresso, 3.5)
    order3 = bob.create_order(latte, 6.0)

    # Test relationships
    print(f"Alice's orders: {[order.price for order in alice.orders()]}")  # [5.0, 3.5]
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")  # ['Latte', 'Espresso']
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")  # ['Alice', 'Bob']
    print(f"Latte's orders: {[order.price for order in latte.orders()]}")  # [5.0, 6.0]
    print(f"Latte's number of orders: {latte.num_orders()}")  # 2
    print(f"Latte's average price: {latte.average_price()}")  # 5.5
    print(f"Most aficionado for Latte: {Customer.most_aficionado(latte).name}")  # Bob