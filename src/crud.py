import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config1.config import connect_db
import psycopg2


def insert_property(property):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        insert_query = """
            INSERT INTO properties (Ranks, Countries, Gold, Silver, Bronze, Total)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            property['Ranks'], property['Countries'], property['Gold'],
            property['Silver'], property['Bronze'], property['Total']
        ))
        conn.commit()
        print("Property added successfully!")

    except Exception as error:
        print(f"Error inserting property: {error}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()



def delete_property(property_id):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        delete_query = """
            DELETE FROM properties
            WHERE id = %s
        """
        cursor.execute(delete_query, (property_id,))
        conn.commit()

        row_count = cursor.rowcount
        if row_count > 0:
            print(f"{row_count} row(s) deleted successfully.")
        else:
            print("No rows found matching the deletion criteria.")

    except Exception as error:
        print(f"Error deleting property: {error}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def update_property(property):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        update_query = """
            UPDATE properties
            SET Ranks = %s, Countries = %s, Gold = %s, Silver = %s, Bronze = %s, Total = %s
            WHERE id = %s
        """
        cursor.execute(update_query, (
            property['Ranks'], property['Countries'], property['Gold'],
            property['Silver'], property['Bronze'], property['Total'], property['id']
        ))
        conn.commit()

        row_count = cursor.rowcount
        if row_count > 0:
            print(f"{row_count} row(s) updated successfully.")
        else:
            print("No rows found matching the update criteria.")

    except Exception as error:
        print(f"Error updating property: {error}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
        
        
def read_properties():
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = conn.cursor()

    try:
        select_query = """
            SELECT * FROM properties
        """
        cursor.execute(select_query)
        properties = cursor.fetchall()
        for property in properties:
            print(property)

    except Exception as error:
        print(f"Error reading properties: {error}")

    finally:
        cursor.close()
        conn.close()