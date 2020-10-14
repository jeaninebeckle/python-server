class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, email, password):
        self.id = id
        self.name = name
        self.address = address
        self.email = email,
        self.password = password

    def __repr__(self):
        return f"{self.name} lives at {self.address}"

# customer = Customer(1, 'Hannah Hall', '7002 Chestnut Ct')
