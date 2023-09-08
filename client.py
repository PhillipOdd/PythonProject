import sqlite3

class Client:
    def __init__(self, name, apartment_id, lease_period):
        self.name = name
        self.apartment_id = apartment_id
        self.lease_period = lease_period

    def add_to_database(self):
        conn = sqlite3.connect('apartment_management.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO client (name, apartment_id, lease_period) VALUES (?, ?, ?)',
                       (self.name, self.apartment_id, self.lease_period))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_from_database(client_name):
        conn = sqlite3.connect('apartment_management.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM client WHERE name = ?', (client_name,))
        conn.commit()
        conn.close()

# You can add more methods to the Client class as needed


