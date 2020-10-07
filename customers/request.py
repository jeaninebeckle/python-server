CUSTOMERS = [
  {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct"
    },
    {
        "id": 2,
        "name": "Brain Neal",
        "address": "500 Main St",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Mitchell Blom",
        "address": "912 Germany St",
    }
]

def get_all_customers():
    return CUSTOMERS

    
def get_single_customer(id):
   
    requested_customer = None

    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
