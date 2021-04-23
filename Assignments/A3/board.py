def make_board() -> list:
    """Create a 5x5 board

    :postcondition: create a list with coordinate for 5x5 board
    :postcondition: assign the character to (0, 0) coordinate
    :return: the list
    """
    coordinates = [(x, y) for x in range(5) for y in range(5)]
    return coordinates


def print_board(character_coordinates: dict) -> None:
    """Print the board

    :param character_coordinates: a dictionary
    :precondition: coordinates must be a list
    :precondition: character_coordinates must be a dictionary
    :postcondition: for each coordinate, print a value
    :return: None
    """
    for y in range(5):
        for x in range(5):
            if (character_coordinates['x'], character_coordinates['y']) == (x, y):
                print(" 🚶 ", end='')
            else:
                print(" o ", end='')
        print()
