LOCATIONS = [
    {
        "id": 1,
        "city": "Orlando",
        "state": "Florida",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "city": "Fargo",
        "state": "North Dakota",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "city": "Naperville",
        "state": "Illinois",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_locations():
    return LOCATIONS

    
def get_single_location(id):
   
    requested_location = None

    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location
