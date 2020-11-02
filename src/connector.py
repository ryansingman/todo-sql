import os
import sqlite3


def create_connection(path: str) -> sqlite3.Connection: 
    """Creates connection to SQLite3 database

    Parameters
    ----------
    path : str
        path to database file

    Returns
    -------
    sqlite3.Connection
        returns created/connected database file
    """
    connection = sqlite3.connect(
        os.path.join(path, "todo_app.sqlite")
    )

    return connection