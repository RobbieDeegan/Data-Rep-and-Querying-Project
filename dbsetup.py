# Adapted from https://docs.python.org/2/library/sqlite3.html

import sqlite3

DATABASE = 'data/passwordData.db'

conn = sqlite3.connect('data/passwordData.db')

def setupDataBase():
    c = conn.cursor()

    # Create table
    c.execute("CREATE TABLE IF NOT EXISTS passwordTable(password TEXT)")

    # Insert sample information
    c.execute("INSERT INTO passwordTable(password) VALUES('HkfQAFta~s')")

    # Commit changes to the database
    conn.commit()

    # Close connection
    conn.close()
    
if __name__ == "__main__":
    setupDataBase()
