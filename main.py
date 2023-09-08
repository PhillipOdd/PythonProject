from client import Client
from apartment import Apartment
import sqlite3

# Function to display the apartment summary
def display_apartment_summary():
    conn = sqlite3.connect('apartment_management.db')
    cursor = conn.cursor()

    cursor.execute('SELECT name, total_rooms, available_rooms FROM apartment')
    apartments = cursor.fetchall()

    for apartment in apartments:
        name, total_rooms, available_rooms = apartment
        print(f"Apartment '{name}' has {total_rooms} rooms total and {available_rooms} rooms available.")

    conn.close()

# Function to add a client and update available rooms
# Function to add a client and update available rooms
def add_client():
    apartment_name = input("Enter the apartment name: ")
    client_name = input("Enter the client's name: ")
    lease_period = int(input("Enter the lease period (in months): "))

    # Check if the apartment exists or create a new one if not
    conn = sqlite3.connect('apartment_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, available_rooms FROM apartment WHERE name = ?', (apartment_name,))
    apartment = cursor.fetchone()

    if apartment:
        apartment_id, available_rooms = apartment
    else:
        # Create a new apartment if it doesn't exist
        apartment_obj = Apartment(apartment_name, total_rooms=10, available_rooms=9)  # You can adjust the room counts
        apartment_obj.add_to_database()
        apartment_id = cursor.lastrowid
        available_rooms = apartment_obj.available_rooms

    conn.close()

    if available_rooms > 0:
        client = Client(client_name, apartment_id, lease_period)
        client.add_to_database()

        # Update available rooms
        new_available_rooms = available_rooms - 1
        apartment_obj = Apartment(apartment_name, apartment_id, new_available_rooms)
        apartment_obj.update_available_rooms(new_available_rooms)

        print("Client added successfully.")
    else:
        print("No available rooms in this apartment.")


# Function to delete a client and update available rooms
# Function to delete a client and update available rooms
def delete_client():
    client_name = input("Enter the client's name to delete: ")

    # Check if the client exists
    conn = sqlite3.connect('apartment_management.db')
    cursor = conn.cursor()
    cursor.execute('SELECT apartment_id FROM client WHERE name = ?', (client_name,))
    apartment_id = cursor.fetchone()

    if apartment_id:
        apartment_id = apartment_id[0]

        # Retrieve the apartment name using the apartment_id
        cursor.execute('SELECT name FROM apartment WHERE id = ?', (apartment_id,))
        apartment_row = cursor.fetchone()

        print("Debug: apartment_id:", apartment_id)
        print("Debug: apartment_row:", apartment_row)

        if apartment_row:
            apartment_name = apartment_row[0]

            # Delete the client
            Client.delete_from_database(client_name)

            # Update available rooms
            apartment_obj = Apartment(apartment_name, apartment_id, None)
            apartment_info = apartment_obj.get_apartment_info()
            available_rooms = apartment_info["available_rooms"]

            new_available_rooms = available_rooms + 1
            apartment_obj.update_available_rooms(new_available_rooms)

            print("Client deleted successfully.")
        else:
            print(f"Apartment not found for client '{client_name}'.")
    else:
        print(f"Client '{client_name}' not found.")

# Rest of your code remains the same


# Rest of your code remains the same




if __name__ == "__main__":
    while True:
        display_apartment_summary()

        choice = input("Do you want to (A)dd a client, (D)elete a client, or (Q)uit? ").lower()
        
        if choice == 'a':
            add_client()
        elif choice == 'd':
            delete_client()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please enter 'A', 'D', or 'Q'.")

