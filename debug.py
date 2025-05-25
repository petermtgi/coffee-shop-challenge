from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Peter")
c2 = Customer("Lana")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

c1.create_order(latte, 4.5)
c1.create_order(latte, 5.0)
c2.create_order(latte, 6.0)
c1.create_order(espresso, 3.0)

print(c1.orders())
print(c1.coffees())
print(latte.customers())
print(latte.num_orders())
print(latte.average_price())
print(Customer.most_aficionado(latte))  # Should be Lana
