# PythonProject
# Apartment Management System

The Apartment Management System is a Python-based program designed to help manage apartment details, clients, and room availability. This system allows you to keep track of apartments, clients residing in them, and the status of available rooms.

## Features

 **Apartment Management**: Add, view, and update apartment details such as name, total rooms, and available rooms.

 **Client Management**: Add, view, and remove clients from apartments. The system automatically updates the available rooms accordingly.

 **Dynamic Apartment Creation**: When adding a client to a non-existent apartment, the system dynamically creates the apartment.

 **Database Integration**: The system uses an SQLite database to store apartment and client data, ensuring data persistence.

 ## Technologies used

  PYTHON
  SQL - A database of the properties and the people staying inside. This will be done using mysqli. Clients, apartments, and rooms will have tables that  have different relationships.
  CLI - allows a tenant to interact with the application and see the properties of different tenants and rooms.
  SQLITE


## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/PhillipOdd/PythonProject.git
   
2. Make sure necessary dependencies are installed e.g.
   sqlite3
   pipenv

3. Navigate into the project folder
   cd pythonproject

4. View the management system
   run the "main.py file


# Usage

When you run the program, you will be presented with a menu to perform various actions.

Use options like Add a client, Delete a client, or Quit to interact with the system.

The system will display apartment summaries with information on total rooms and available rooms.

# License
This project is licensed under the MIT License.


