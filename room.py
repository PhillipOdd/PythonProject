import sqlite3

class Room:
    def __init__(self, room_number, apartment_id):
        self.room_number = room_number
        self.apartment_id = apartment_id

    def add_to_database(self):
        conn = sqlite3.connect('apartment_management.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO room (room_number, apartment_id) VALUES (?, ?)',
                       (self.room_number, self.apartment_id))
        conn.commit()
        conn.close()

# You can add more methods to the Room class as needed
