import sys
import os
import csv


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config1.config import connect_db

def fetch_properties():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PROPERTIES")
    olympic_data = cursor.fetchall()
    cursor.close()
    conn.close
    return olympic_data


def generate_csv(filename='data/properties.csv'):
    properties = fetch_properties()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'Ranks', 'Countries', 'Gold', 'Silver', 'Bronze', 'Total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for property in properties:
            writer.writerow({
                'id':property[0],
                'Ranks':property[1],
                'Countries' :property[2],
                'Gold':property[3],
                'Silver':property[4],
                'Bronze':property[5],
                'Total':property[6]
            })
        print("csv exported")

generate_csv()