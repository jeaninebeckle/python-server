EMPLOYEES = [
    {
        "id": 1,
        "name": "Suzy",
        "position": "Manager",
        "employeeId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Jim",
        "position": "Cashier",
        "employeeId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Fred",
        "position": "Janitor",
        "employeeId": 2,
        "customerId": 1
    }
]


def get_all_employees():
    return EMPLOYEES

    
def get_single_employee(id):
   
    requested_employee = None

    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
