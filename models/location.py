class Location():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
    
    def __repr__(self):
        return f"{self.name} is at {self.address}"

# location = Location(1, 'Nashville North', "8422 Johnson Pike")
