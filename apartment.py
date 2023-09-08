import sqlite3

class Apartment:
    def __init__(self, name, total_rooms, available_rooms):
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms

    def add_to_database(self):
        conn = sqlite3.connect('apartment_management.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO apartment (name, total_rooms, available_rooms) VALUES (?, ?, ?)',
                       (self.name, self.total_rooms, self.available_rooms))
        conn.commit()
        conn.close()

    def update_available_rooms(self, new_available_rooms):
        conn = sqlite3.connect('apartment_management.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE apartment SET available_rooms = ? WHERE name = ?', (new_available_rooms, self.name))
        conn.commit()
        conn.close()

# You can add more methods to the Apartment class as needed
