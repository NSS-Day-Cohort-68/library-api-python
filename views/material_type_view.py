import sqlite3
import json

def list_material_types():
    # Open a connection to the database
    with sqlite3.connect("./library.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            mt.id,
            mt.name,
            mt.checkout_days
        FROM MaterialTypes mt
        """)
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        material_types=[]
        for row in query_results:
            material_types.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_material_types = json.dumps(material_types)

    return serialized_material_types
