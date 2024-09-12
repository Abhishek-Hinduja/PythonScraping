import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.scrape import scrape_paris_olympic_games_media
from src.store import store_Olympic_medal_data
from src.export import generate_csv
from src.crud import insert_property, delete_property, update_property, read_properties


def main():
    
    properties = scrape_paris_olympic_games_media()

    for property in properties:
        print(property)
        
    store_Olympic_medal_data(properties)  
    generate_csv() 

    # while True:
    #     print("\nCRUD Menu:")
    #     print("1. Insert Property")
    #     print("2. Update Property")
    #     print("3. Delete Property")
    #     print("4. Read Properties")
    #     print("5. Exit")
        
    #     choice = input("Enter your choice (1/2/3/4/5): ")
        
    #     if choice == '1':
    #         property = {
    #             'Ranks': input("Enter Ranks: "),
    #             'Countries': input("Enter Countries: "),
    #             'Gold': input("Enter Gold: "),
    #             'Silver': input("Enter Silver: "),
    #             'Bronze': input("Enter Bronze: "),
    #             'Total': input("Enter Total: ")
    #         }
    #         insert_property(property)
            
    #     elif choice == '2':
    #         property = {
    #             'id': input("Enter the ID of the property to update: "),
    #             'Ranks': input("Enter new Ranks: "),
    #             'Countries': input("Enter new Countries: ")
    #             'Gold': input("Enter new Gold: "),
    #             'Silver': input("Enter new Silver: "),
    #             'Bronze': input("Enter new Bronze: "),
    #             'Total': input("Enter new Total: "),
    #             
    #         }
    #         update_property(property)
            
    #     elif choice == '3':
    #         property_id = input("Enter the ID of the property to delete: ")
    #         delete_property(property_id)
            
    #     elif choice == '4':
    # #         read_properties()
            
    #     elif choice == '5':
    #         print("Exiting program.")
    #         break
            
    #     else:
    #         print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
