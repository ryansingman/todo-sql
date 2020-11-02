from src.action import Action
from .parse_add import AddAction 
from .parse_list import ListAction
from .parse_clear import ClearAction
from .parse_check import CheckAction

def parse_command(command: str) -> Action:
    """Creates action object from command

    Parameters
    ----------
    command : str
        command string

    Returns
    -------
    Action
        action object defining action to take
    """
    if command == "add":
        action = AddAction()

    elif command == "list":
        action = ListAction()

    elif command == "clear":
        action = ClearAction()

    elif command == "check":
        action = CheckAction()

    else:
        raise ValueError(
            f"command {command} not one of: [\"add\", \"list\", \"clear\"]"
        )

    return action