import sqlite3
import json

from models.location import Location

LOCATIONS = [
    # Location(1, "Nashville North", "8422 Johnson Pike"),
    # Location(2, 'Nashville South', "209 Emory Drive"),
    # Location(3, 'Nashville West', "100 Charlotte Pike")
]

def get_all_locations():
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)

        locations = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    return json.dumps(locations)

    
def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)

def create_location(location):
    max_id = LOCATIONS[-1].id

    new_id = max_id + 1

    location["id"] = new_id

    new_location = Location(location['id'], location['name'], location['address'])
    LOCATIONS.append(new_location)

    return location

    
# def get_single_location(id):
   
#     requested_location = None

#     for location in LOCATIONS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if location.id == id:
#             requested_location = location

#     return requested_location

def delete_location(id):
    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location.id == id:
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location.id == id:
            LOCATIONS[index] = Location(new_location['id'], new_location['name'], new_location['address'])
            break
