from src.action import Action


def build_add_query(add_action: Action) -> str:
    """Builds add query from action item

    Parameters
    ----------
    add_action : action
        add action to build query from

    Returns
    -------
    str
        query to execute
    """
    return f"""
    INSERT INTO
        'todos' ('name', 'notes', 'due_date', 'completed')
    VALUES
        ('{add_action.name}', '{add_action.notes}', '{add_action.due_date}', {0});
    """


def build_list_query(list_action: Action) -> str:
    """Builds list query from action item

    Parameters
    ----------
    list_action : action
        list action to build query from

    Returns
    -------
    str
        query to execute
    """
    return f"""
        SELECT * FROM todos
        WHERE name LIKE '{list_action.pattern}'
        AND due_date <= '{list_action.end_date}'
        AND due_date >= '{list_action.start_date}';
    """


def build_clear_query(clear_action: Action) -> str:
    """Builds clear query from action item

    Parameters
    ----------
    clear_action : action
        clear action to build query from

    Returns
    -------
    str
        query to execute
    """
    return f"""
        DELETE FROM todos
        WHERE name LIKE '{clear_action.pattern}'
        AND due_date <= '{clear_action.end_date}'
        AND due_date >= '{clear_action.start_date}';
    """


def build_check_query(check_action: Action) -> str:
    """Builds check query from action item

    Parameters
    ----------
    check_action : action
        check action to build query from

    Returns
    -------
    str
        query to execute
    """
    return f"""
        UPDATE todos
        SET completed = 1
        WHERE name LIKE '{check_action.pattern}';
    """