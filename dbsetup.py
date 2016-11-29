# Adapted from https://docs.python.org/2/library/sqlite3.html
import sqlite3

DATABASE = 'data/passwordData.db'

conn = sqlite3.connect('data/passwordData.db')

def setupDataBase():
    c = conn.cursor()

    # Create the table to store the passwords
    c.execute("CREATE TABLE IF NOT EXISTS passwordTable(password TEXT)")

    # Insert a sample password into the password table
    c.execute("INSERT INTO passwordTable(password) VALUES('Example: HkfQAFta~s')")

    # Commit changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()
    
if __name__ == "__main__":
    setupDataBase()
