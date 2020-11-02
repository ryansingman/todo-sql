from datetime import date, timedelta, datetime as dt

from src.action import Action


class ClearAction(Action):
    """Clear action class"""
    DT_FORMAT = "%Y-%m-%d"
    def __init__(self):
        """Initializes clear action object"""
        super().__init__()

        # set action type
        self.action_type = "CLEAR"

        # parse details
        self.parse_details()

    def parse_details(self):
        """Receives CLI input for action details"""
        print("Clear Action:")

        # parse item regex 
        self.pattern = input("Item regex (to list) ('%' == '.*', '_' == '.'): ")

        # parse date range start
        start_date_str = input(
            "Start date of date range (default = <today>) (YYYY-MM-DD): "
        )
        if start_date_str:
            self.start_date = dt.strptime(start_date_str, self.DT_FORMAT)

        else:
            self.start_date = date.today()


        # parse date range delta
        time_delta_str = input("Time delta (<n>[D|M|Y]): ")
        if not time_delta_str:
            time_delta = timedelta(weeks=52)

        elif time_delta_str[-1] == "D":
            time_delta = timedelta(days=int(time_delta_str[:-1]))

        elif time_delta_str[-1] == "M":
            time_delta = timedelta(months=int(time_delta_str[:-1]))

        elif time_delta_str[-1] == "Y":
            time_delta = timedelta(years=int(time_delta_str[:-1]))

        else:
            raise ValueError(f"Invalid time delta {time_delta_str}")

        self.end_date = self.start_date + time_delta
