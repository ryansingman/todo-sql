import sqlite3

# static query to create table
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  notes TEXT,
  due_date timestamp,
  completed INTEGER
);
"""

def create_table(connection: sqlite3.Connection):
    """Creates todos table if it doesn't exist

    Parameters
    ----------
    connection : sqlite3.Connection
        connection to execute query on
    """
    # execute query
    cursor = connection.cursor()
    cursor.execute(CREATE_TABLE_QUERY)
    connection.commit()