class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Name must be a string of at least 3 characters.")
        if hasattr(self, "_name"):  
            raise AttributeError("Name cannot be changed after instantiation.")
        self._name = value


    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))

    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        if self.num_orders() == 0:
            return 0
        total = sum(order.price for order in self.orders())
        return total / self.num_orders()

class Customer:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]

    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Name must be a string of at least 3 characters.")
        if hasattr(self, "_name"):
            return  # Silently ignore instead of raising an error
        self._name = value