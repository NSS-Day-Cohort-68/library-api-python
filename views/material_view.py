import sqlite3
import json

def list_materials():
    # Open a connection to the database
    with sqlite3.connect("./library.sqlite3") as conn:
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
    with sqlite3.connect("./library.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT m.*, mt.name AS material_type_name, mt.checkout_days, g.name AS genre_name
        FROM Materials m
        JOIN MaterialTypes mt ON mt.id = m.material_type_id
        JOIN Genres g ON g.id = m.genre_id 
        WHERE m.id = ?
        """,
            (pk,),
        )
        data = dict(db_cursor.fetchone())

        material = {
            "id": data["id"],
            "title": data["title"],
            "author": data["author"],
            "checkout_date": data["checkout_date"],
            "genre": {"id": data["genre_id"], "name": data["genre_name"]},
            "material_type": {
                "id": data["material_type_id"],
                "name": data["material_type_name"],
                "checkout_days": data["checkout_days"],
            },
        }

        serialized_material = json.dumps(material)
        return serialized_material
