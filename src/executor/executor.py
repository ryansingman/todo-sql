from typing import List, Tuple
import sqlite3

from src.action import Action
from .build_queries import (
    build_add_query,
    build_list_query,
    build_clear_query,
    build_check_query,
)

def apply_action(action: Action, connection: sqlite3.Connection) -> List[Tuple]:
    """Builds query and executes for action

    Parameters
    ----------
    action : Action
        action to build query for and execute

    connection : sqlite3.Connection
        connection to execute query on
    """
    # build query for action
    if action.action_type == "ADD":
        query = build_add_query(action)

    elif action.action_type == "LIST":
        query = build_list_query(action)

    elif action.action_type == "CLEAR":
        query = build_clear_query(action)

    elif action.action_type == "CHECK":
        query = build_check_query(action)

    # execute query
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    # fetch records if action type is list
    if action.action_type == "LIST":
        records = cursor.fetchall()

    else:
        records = None

    # close cursor
    cursor.close()

    return records