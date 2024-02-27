import sqlite3
import json

def list_materials():
    # Open a connection to the database
    with sqlite3.connect("./library.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT * FROM Materials
        """)
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        materials=[]
        for row in query_results:
            materials.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_materials = json.dumps(materials)

    return serialized_materials

# TODO: implement update_material view
def update_material(id, material_data):
    return True

# TODO: implement delete_material view
def delete_material(pk):
    return True

# TODO: finish implementation of retrieve_material view
def retrieve_material(pk):
    material = {}
    serialized_material = json.dumps(material)
    return serialized_material
