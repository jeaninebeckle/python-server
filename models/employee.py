class Employee():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, location, manager, full_time, hourly_rate):
        self.id = id
        self.name = name
        self.location = location
        self.manager = manager
        self.full_time = full_time
        self.hourly_rate = hourly_rate

    def __repr__(self):
        return f"{self.name} is an employee and makes ${self.hourly_rate} an hour."

employee = Employee(1, 'Sally', 2, True, True, 20)
