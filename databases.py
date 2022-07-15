
from objects import *
from sqlite3 import *

def database_operation(function):
    def wrapper(self, *args):
        conn = connect(self.filepath)
        cursor = conn.cursor()

        result = function(self, cursor, *args)
        conn.commit()
        conn.close()

        return result

    return wrapper

class DatabaseHelper:
    def __init__(self, filepath: str):
        self.filepath = filepath

    @database_operation
    def create_tables(self, cursor: Cursor):
        command = """
CREATE TABLE IF NOT EXISTS ContactTbl (
    UserID          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name            TEXT,
    Email           TEXT,
    PhoneNumber     TEXT
)
                  """

        cursor.execute(command)

    @database_operation
    def insert_contact(self, cursor: Cursor, contact: Contact):
        command = """
INSERT INTO ContactTbl
VALUES (?, ?, ?, ?)
                  """

        cursor.execute(command, (None, contact.name, contact.email, contact.phone_number))
        
    @database_operation
    def delete_contact(self, cursor: Cursor, contact: Contact):
        command = """
DELETE FROM ContactTbl WHERE UserID = ?
                  """

        cursor.execute(command, (contact.id,))

    @database_operation
    def get_all_contacts(self, cursor: Cursor):
        command = """
SELECT * FROM ContactTbl
                  """

        cursor.execute(command)     
        rows = cursor.fetchall()
        contacts = []

        for row in rows:
            contact = Contact(row[0], row[1], row[2], row[3])
            contacts.append(contact)

        return contacts
