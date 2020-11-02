from typing import List, Tuple
from datetime import datetime as dt, timedelta

# color macros
GREEN = "\u001b[32m"
RED = "\u001b[31m"
RESET = "\u001b[0m"

# datetime format
DT_FORMAT = "%Y-%m-%d %H:%M:%S"


def print_record(record: Tuple):
    """Prints record

    Parameters
    ----------
    record : Tuple
        record with the format:
        (<id>, <name>, <notes>, <due_date>, <completed>)
    """
    # if completed, highlight in green
    if record[-1]:
        color = GREEN
    # if not completed, and due date in less than three days, make text red
    elif dt.strptime(record[3], DT_FORMAT) - dt.today() < timedelta(days=3):
        color = RED
    else:
        color = RESET

    print(f"{color}|{record[1].ljust(15)}|{record[3].ljust(25)}|{record[2].ljust(20)}|{RESET}")


def format_output(records: List[Tuple]):
    """Formats and prints output

    Parameters
    ----------
    records : List[Tuple]
        list of records with the format:
        (<id>, <name>, <notes>, <due_date>, <completed>)
    """
    # check if records exist
    if not records:
        print("No records found... exiting")
        return None

    # sort records by due date (descending order)
    records = sorted(
        records,
        key=lambda x: x[3]
    )

    # print table header
    print(64*"-")
    print(f"|{'Name'.ljust(15)}|{'Due Date'.ljust(25)}|{'Notes'.ljust(20)}|")
    print(64*"-")

    # print records
    for record in records:
        print_record(record)

    print(64*"-")