EMPLOYEES = [
    {
        "id": 1,
        "name": "Sally",
        "location": 2,
        "manager": True,
        "full time": True,
        "hourly rate": 20
    },
    {
        "id": 2,
        "name": "Fred",
        "location": 1,
        "manager": False,
        "full time": True,
        "hourly rate": 13
    },
    {
        "id": 3,
        "name": "Erin",
        "location": 3,
        "manager": False,
        "full time": False,
        "hourly rate": 15
    }
]


def get_all_employees():
    return EMPLOYEES

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

    
def get_single_employee(id):
   
    requested_employee = None

    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
