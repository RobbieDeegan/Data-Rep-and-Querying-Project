# Adapted from https://github.com/data-representation/example-sqlite

import sqlite3

DATABASE = 'data/passwordData.db'

def setup_db():
  db = sqlite3.connect(DATABASE)
  cur = db.cursor()

  # Create the table if it doesn't exist.
  cur.execute("CREATE TABLE IF NOT EXISTS passwordTable(password TEXT)")
  db.commit()

  # Insert some dummy data if the table is empty.
  cur.execute("SELECT COUNT(*) FROM passwordTable")
  if cur.fetchall()[0][0] == 0:
    cur.execute('INSERT INTO passwordTable(password) VALUES("HkfQAFta~s")')
    db.commit()

if __name__ == "__main__":
  setup_db()
