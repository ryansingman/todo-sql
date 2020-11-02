from datetime import datetime as dt

from src.action import Action


class AddAction(Action):
    """Add action class"""
    DT_FORMAT = "%Y-%m-%d %H:%M"
    def __init__(self):
        """Initializes add action object"""
        super().__init__()

        # set action type
        self.action_type = "ADD"

        # parse details
        self.parse_details()

    def parse_details(self):
        """Receives CLI input for action details"""
        print("Add action:")

        # parse item name
        self.name = input("Item name: ")
        while not self.name:
            print("Name field is required for add action")
            self.name = input("Item name: ")

        # parse item due date
        self.due_date = dt.strptime(
            input("Item due date (yyyy-mm-dd HH:MM): "), self.DT_FORMAT
        )
        while not self.due_date:
            print("Due date field is required for add action")
            self.due_date = dt.strptime(
                input("Item due date (yyyy-mm-dd HH:MM): "), self.DT_FORMAT
            )

        # parse item notes
        self.notes = input("Notes (press enter if not needed): ")