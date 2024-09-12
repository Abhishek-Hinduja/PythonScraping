import sys
import os
import psycopg2


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config1.config import connect_db


def store_Olympic_medal_data(properties):
    conn = connect_db()

    if conn is None:
        print("Failed to Connect database")
        return
    
    cursor = conn.cursor()

    try:

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                       id SERIAL PRIMARY KEY,
                       Ranks INT,
                       Countries VARCHAR(255),
                       Gold INT,
                       Silver INT,
                       Bronze INT,
                       Total INT
                       )
        """)
        print("Table properties created or Already Exists")

        for prop in properties:
                
                cursor.execute("""
                INSERT INTO properties (Ranks, Countries, Gold, Silver, Bronze, Total)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    prop['Ranks'], prop['Countries'], prop['Gold'],
                    prop['Silver'], prop['Bronze'], prop['Total']
                ))

        conn.commit()
        print("Properties have been successfully stored in the database")

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()


           
