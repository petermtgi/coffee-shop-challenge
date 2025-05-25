class Customer:
    _all = []

    def __init__(self, name):
        self.name = name
        Customer._all.append(self)

    def __repr__(self):
        return f"Customer('{self._name}')"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order._all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        top_customer = None
        top_spent = 0
        for customer in cls._all:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > top_spent:
                top_spent = total
                top_customer = customer
        return top_customer
