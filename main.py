import pathlib

from src.parser import parse_command
from src.connector import create_connection
from src.executor import apply_action, create_table
from src.output import format_output

if __name__ == "__main__":
    import argparse
    from argparse import RawTextHelpFormatter

    command_help_str = (
        "command to execute\n"
        "Examples:\n"
        "\tadd := adds todo (will prompt for details)\n"
        "\tlist := lists todos\n"
        "\tclear := clears todos\n"
        "\tcheck := checks todos as completed\n"
    )

    parser = argparse.ArgumentParser(
        description=command_help_str,
        formatter_class=RawTextHelpFormatter
    )
        
    parser.add_argument(
        "command",
        help="command to execute",
    )

    args = parser.parse_args()

    # create sqlite server (file) if doesn't already exist
    connection = create_connection(
        pathlib.Path().absolute()
    )

    # create todo table if necessary
    create_table(connection)

    # parse command into action
    action = parse_command(args.command)

    # apply action to database
    result = apply_action(action, connection)

    # format and print result
    if args.command == "list":
        format_output(result)