from src.action import Action


class CheckAction(Action):
    """Check action class"""
    def __init__(self):
        """Initializes check action object"""
        super().__init__()

        # set action type
        self.action_type = "CHECK"

        # parse details
        self.parse_details()

    def parse_details(self):
        """Receives CLI input for action details"""
        print("Check Action:")

        # parse item regex 
        self.pattern = input("Item regex (to check as completed) ('%' == '.*', '_' == '.'): ")