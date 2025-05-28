class Coffee:
    _all = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            Coffee._all.append(self)
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    def __repr__(self):
        return f"Coffee('{self._name}')"

    @property
    def name(self):
        return self._name 

    def orders(self):
        return [order for order in Order._all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return round(sum(order.price for order in orders) / len(orders), 2)
