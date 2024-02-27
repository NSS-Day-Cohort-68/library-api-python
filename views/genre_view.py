import sqlite3
import json

def list_genres():
    # Open a connection to the database
    with sqlite3.connect("./library.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            g.id,
            g.name
        FROM Genres g
        """)
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        genres=[]
        for row in query_results:
            genres.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_genres = json.dumps(genres)

    return serialized_genres

