import doctest


def game():
    """Run the game

    :postcondition: make the board
    :postcondition: make the character
    :postcondition: while the character has not reached the exit ask the user for direction and move as long as it does
    not go out the board
    :postcondition: when the exit is reached, print the number of steps it took for the character to reach the exit
    :return: None
    """
    board = make_board()
    character = make_character()
    found_exit = False
    step = 0
    while not found_exit:
        print_board(board)
        direction = get_user_choice()
        valid_move = validate_move(coordinates=board, character_dict=character, user_input=direction)
        if valid_move:
            step += 1
            move_character(coordinates=board, character_dict=character, user_input=direction)
            found_exit = check_if_exit_reached(character)
        else:
            print("There's a wall in that direction.")
    print_board(board)
    print('Congratulation! You found the exit.')
    print(f'It took you {step} steps to exit.')


def make_board() -> dict:
    """Create a 5x5 board

    :postcondition: create a dictionary with coordinate for 5x5 board
    :postcondition: assign the character to (0, 0) coordinate
    :return: the dictionary
    """
    coordinates = {(x, y): ' o ' for x in range(5) for y in range(5)}
    coordinates[(0, 0)] = " 🚶 "
    coordinates[(4, 4)] = " x "
    return coordinates


def make_character() -> dict:
    """Create a character

    :postcondition: create a dictionary with key, value pair reflecting current coordinate
    :return: the dictionary
    >>> make_character()
    {'x': 0, 'y': 0}
    """
    character = {'x': 0, 'y': 0}
    return character


def get_user_choice() -> str:
    """Get user choice

    :postcondition: prompt user for direction
    :postcondition: check if the user input is valid
    :return: the user input
    """
    user_choice = input('where would you like to go?(n/s/w/e) ').strip().lower()
    if user_choice in ['n', 's', 'w', 'e']:
        return user_choice
    print('Invalid input.')
    return get_user_choice()


def validate_move(coordinates: dict, character_dict: dict, user_input: str) -> bool:
    """Check if user can move in a specific direction

    :param coordinates: a dictionary
    :param character_dict: a dictionary
    :param user_input: a string
    :precondition: coordinates and character_dict must be dictionaries, and user_input a string
    :postcondition: get the changed coordinate
    :postcondition: check if the coordinate exists inside the coordinates
    :return: boolean value (True if condition is true, else false)
    >>> validate_move({(0, 0): "", (0, 1): ""}, {"x": 0, "y": 0}, 's')
    True
    >>> validate_move({(0, 0): "", (0, 1): ""}, {"x": 0, "y": 0}, 'n')
    False
    >>> validate_move({}, {"x": 0, "y": 0}, 's')
    False
    """
    new_coordinate = get_new_coordinate(x_y_coordinate=character_dict, move_direction=user_input)
    return new_coordinate in coordinates


def move_character(coordinates: dict, character_dict: dict, user_input: str) -> None:
    """Move the character

    :param coordinates: a dictionary
    :param character_dict: a dictionary
    :param user_input: a string
    :precondition: coordinates and character_dict must be dictionaries, user_input a string
    :postcondition: remove person emoji from the past coordinate in board
    :postcondition: assign new coordinates in character dictionary
    :postcondtion: put a person emoji to the current coordinate in board
    :return: None
    """
    coordinates[(character_dict['x'], character_dict['y'])] = " o "
    character_dict['x'], character_dict['y'] = get_new_coordinate(character_dict, user_input)
    coordinates[(character_dict['x'], character_dict['y'])] = " 🚶 "


def get_new_coordinate(x_y_coordinate: dict, move_direction: str) -> tuple:
    """Calculate the coordinate after the move

    :param x_y_coordinate: a dictionary
    :param move_direction: a string
    :precondition: x_y_coordinate must be a dictionary, move_direction a string
    :postcondition: add numbers to coordinate
    :return: x and y
    >>> get_new_coordinate({'x': 0, 'y': 0}, 's')
    (0, 1)
    >>> get_new_coordinate({'x': 0, 'y': 0}, 'n')
    (0, -1)
    >>> get_new_coordinate({'x': 0, 'y': 0}, 'e')
    (1, 0)
    """
    direction_dict = {'n': (0, -1), 's': (0, 1), 'w': (-1, 0), 'e': (1, 0)}
    x = x_y_coordinate['x'] + direction_dict[move_direction][0]
    y = x_y_coordinate['y'] + direction_dict[move_direction][1]
    return x, y


def check_if_exit_reached(character_dict: dict) -> bool:
    """Check if the character reached the exit

    :param character_dict: a dictionary
    :precondition: character_dict must be a dictionary
    :postcondition: check if the character is at (4, 4)
    :return: boolean depending on the conditional statement above
    >>> check_if_exit_reached({'x': 0, 'y': 0})
    False
    >>> check_if_exit_reached({'x': 2, 'y': 2})
    False
    >>> check_if_exit_reached({'x': 4, 'y': 4})
    True
    """
    return (character_dict['x'], character_dict['y']) == (4, 4)


def print_board(coordinates: dict) -> None:
    """Print the board

    :param coordinates: a dictionary
    :precondition: coordinates must be a dictionary
    :postcondition: for each coordinate, print its value
    :return: None
    """
    for y in range(5):
        for x in range(5):
            print(coordinates[(x, y)], end="")
        print()


def main():
    """Execute the program"""
    game()
    doctest.testmod()


if __name__ == "__main__":
    main()
