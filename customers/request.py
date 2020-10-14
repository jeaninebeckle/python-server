import sqlite3
import json

from models.customer import Customer

CUSTOMERS = [
    # Customer(1, 'Hannah Hall', '7002 Chestnut Ct'),
    # Customer(2, 'Brian Neal', '500 Main St'),
    # Customer(3, 'Mitchell Blom', '912 Germany St')
]

def get_all_customers():
        # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        customers = []

        dataset = db_cursor.fetchall()


        for row in dataset:

            customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)

    
def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        customer = Customer(data['name'], data['address'],data['id'], data['email'], data['password'])

        return json.dumps(customer.__dict__)

def create_customer(customer):
    max_id = CUSTOMERS[-1].id

    new_id = max_id + 1

    customer["id"] = new_id

    new_customer = Customer(customer['id'], customer['name'], customer['address'], customer['email'], customer['password'])
    CUSTOMERS.append(new_customer)

    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer.id == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer.id == id:
            CUSTOMERS[index] = Customer(new_customer['id'], new_customer['name'], new_customer['address'], new_customer['email'], new_customer['password'])
            break

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
