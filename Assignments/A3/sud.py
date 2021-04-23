import A3.board as board
import A3.character as character
import A3.opponent as opponent
import random
import doctest


def game() -> None:
    """Run the game

    :postcondition: make the game board
    :postcondition: make the my character
    :postcondition: run the help function
    :postcondition: get command from user while user does not have enough credits, surrendered, and high stress level
    :postcondition: execute the command from user
    :return: None
    """
    game_board = board.make_board()
    my_character = character.make_character()
    game_guide()
    while my_character['credit'] < 100 and my_character['stress'] < 100 and not my_character['surrendered']:
        command = input('>>> ').strip()
        commands = {
            ('w', 'a', 's', 'd'): [move, [game_board, my_character, command]],
            ('help', 'h', 'guide'): [game_guide, []],
            ('map', 'm'): [board.print_board, [my_character]],
            ('stat', 'character'): [character.print_character, [my_character]],
            ('surrender', 'quit', 'q'): [character.surrender, [my_character]]
        }
        for key in commands:
            if command in key:
                commands[key][0](*commands[key][1])
    if my_character['stress'] > 100:
        print('Your stress level had reached max.\n'
              'Your family were concerned for your mental health and you were forced to withdraw.')
    elif my_character['surrendered']:
        print('You chose sanity over a diploma.\n'
              'Game over.')
    else:
        print('Congratulation! You have successfully gathered 100 credits and earned the CST diploma!\n'
              'The sequel \'Surviving the job hunting\', will be launching in May 2021.')


def game_guide() -> None:
    """Print the commands options

    :postcondition: print registered commands
    :return: None
    >>> game_guide()
    - w/a/s/d for direction
    - help/h/guide for this screen
    - map/m for viewing map
    - stat/character for viewing statistics
    - surrender/quit/q to surrender
    """
    print('- w/a/s/d for direction\n'
          '- help/h/guide for this screen\n'
          '- map/m for viewing map\n'
          '- stat/character for viewing statistics\n'
          '- surrender/quit/q to surrender')


def move(board_list: list, character_dict: dict, direction_str: str) -> None:
    """Relocate the character

    :param board_list: a list
    :param character_dict: a dictionary
    :param direction_str: a string
    :precondition: board_list must be a list
    :precondition: character_dict must be a dictionary
    :precondition: direction_str must be a string
    :postcondition: check if the move is valid
    :postcondition: move and apply side effect if the move is valid
    :postcondition: print helpful error message if there's a wall
    :return: None
    >>> move([(0,0)], {'x': 0, 'y': 0}, 'w')
    There's a wall in that direction
    >>> move([(0,0)], {'x': 0, 'y': 0}, 'a')
    There's a wall in that direction
    >>> move([(0,0)], {'x': 0, 'y': 0}, 's')
    There's a wall in that direction
    """
    valid_move = validate_move(coordinates=board_list, character_coordinates=character_dict, direction=direction_str)
    if valid_move:
        change_coordinate(character_coordinates=character_dict, direction=direction_str)
        side_effect(character_info=character_dict)
    else:
        print('There\'s a wall in that direction')


def validate_move(coordinates: list, character_coordinates: dict, direction: str) -> bool:
    """Check if the user can move in a specific direction

    :param coordinates: a dictionary
    :param character_coordinates: a dictionary
    :param direction: a string
    :precondition: coordinates must be a dictionary
    :precondition: character_coordinates must be a dictionary
    :precondition: direction must be a string
    :postcondition: get a coordinate for when the character moves in the direction user commanded
    :return: true if the new_coordinate if in coordinates else false
    """
    temp_coordinate = get_changed_coordinate(current_coordinate=character_coordinates, arrow_key=direction)
    return temp_coordinate in coordinates


def change_coordinate(character_coordinates: dict, direction: str) -> None:
    """Change the coordinate of the character

    :param character_coordinates: a dictionary
    :param direction: a string
    :precondition: coordinates must be a dictionary
    :precondition: character_info must be a dictionary
    :precondition: key must be a string
    :postcondition: get a coordinate for when the character moves in the direction user commanded
    :postcondition: change the past coordinate, current coordinate of the character
    :postcondition: change the user location in coordinate
    :return: None
    """
    new_coordinate = get_changed_coordinate(current_coordinate=character_coordinates, arrow_key=direction)
    character_coordinates['x'], character_coordinates['y'] = new_coordinate


def get_changed_coordinate(current_coordinate: dict, arrow_key: str) -> tuple:
    """Simulate the move and find the destination

    :param current_coordinate: a dictionary
    :param arrow_key: a string
    :precondition: current_coordinate must be a dictionary
    :precondition: arrow_key must be a string
    :postcondition: add predefined x and y value to original
    :return: the tuple representing x and y value of the changed coordinate
    >>> get_changed_coordinate({'x': 2, 'y': 2}, 'w')
    (2, 1)
    >>> get_changed_coordinate({'x': 2, 'y': 2}, 'd')
    (3, 2)
    >>> get_changed_coordinate({'x': 0, 'y': 0}, 'a')
    (-1, 0)
    """
    direction_info = {'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)}
    x = current_coordinate['x'] + direction_info[arrow_key][0]
    y = current_coordinate['y'] + direction_info[arrow_key][1]
    return x, y


def side_effect(character_info: dict) -> None:
    """Implement the side effect

    :param character_info: a dictionary
    :precondition: character_info must be a dictionary
    :postcondition: at every 1/4 chance, the character encounters an instructor
    :postcondition: else, the student's stress reduces
    :return: None
    """
    if random.randint(1, 4) == 1:
        encounter_instructor(my_character=character_info)
    else:
        reduce_stress(my_character=character_info)


def reduce_stress(my_character: dict) -> None:
    """Reduce stress

    :param my_character: a dictionary
    :precondition: my_character must be a dictionary
    :postcondition: subtract 20 points from character's stress
    :postcondition: if the character's stress is below 0, reset it to 0
    :return: None
    """
    my_character['stress'] -= 20
    if my_character['stress'] < 0:
        my_character['stress'] = 0


def encounter_instructor(my_character: dict) -> None:
    """Execute that command provided by the user

    :param my_character: a dictionary
    :precondition: my_character must be a dictionary
    :postcondition: create an instructor
    :postcondition: ask user for command
    :postcondition: execute the command
    :return: None
    """
    instructor = opponent.create_instructor()
    while True:
        print(f"You have encountered {instructor['name']}.")
        print(f"You can either flee or fight {instructor['name']}.")
        user_input = input('>>> ')
        encounter_command = {
                             'flee': [character.flee, [my_character]],
                             'fight': [fight, [my_character, instructor]],
                             'surrender': [character.surrender, [my_character]]
                             }
        if user_input in encounter_command:
            encounter_command[user_input][0](*encounter_command[user_input][1])
            return
        else:
            print('Invalid input.')


def fight(character_stat: dict, instructor_stat: dict) -> None:
    """Do the assignment

    :param character_stat: a dictionary
    :param instructor_stat: a dictionary
    :precondition: character_stat must be a dictionary
    :precondition: instructor_stat must be a dictionary
    :postcondition: decide turns
    :postcondition: run attack_round
    :return: None
    """
    first_turn = decide_turn()
    if first_turn == 'student':
        attack_round(attacker=character_stat, defender=instructor_stat)
    else:
        attack_round(attacker=instructor_stat, defender=character_stat)


def decide_turn() -> str:
    """compare the die roll

    :postcondition: student and instructor each roll a die
    :postcondition: if the die roll result is the same, call the function again
    :postcondition: return 'student' if student rolled higher or 'instructor' if instructor higher
    :return: string
    """
    student_roll = random.randint(1, 6)
    instructor_roll = random.randint(1, 6)
    if student_roll == instructor_roll:
        return decide_turn()
    return 'student' if student_roll > instructor_roll else 'instructor'


def attack_round(attacker: dict, defender: dict) -> None:
    """Attacker attacks the defender

    :param attacker: a dictionary
    :param defender: a dictionary
    :precondition: attacker must be a dictionary
    :precondition: defender must be a dictionary
    :postcondition: check if the attacker successfully attacks the defender
    :postcondition: attacker attacks defender until one reaches the limit
    :return: None
    """
    if attack_succeeded():
        damage = random.randint(1, 60)
        defender['stress'] += damage
        print(f"{attacker['name']} mentally strained {defender['name']} by {damage} points.")
        if defender['stress'] > 100:
            if defender['type'] == 'instructor':
                print(f"You have successfully finished the {defender['assignment']} "
                      f"{defender['name']} assigned to you.")
                attacker['credit'] += 10
                return
    else:
        print(f"{attacker['name']}'s attack failed.")
    return attack_round(attacker=defender, defender=attacker)


def attack_succeeded():
    """flip the choice

    :return: true if the random integer is 1 else false
    """
    return random.randint(1, 2) == 1


def main():
    """Run game"""
    game()
    doctest.testmod()


if __name__ == "__main__":
    main()
