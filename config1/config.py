import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="Olympic_game",
            user="postgres",
            password="admin",
            host="localhost"
        )
        print("Successfully Connected to database")
        return conn
    except psycopg2.Error as e:
        print(f"Error Connecting to database: {e}")
        return None
    
connect_db()