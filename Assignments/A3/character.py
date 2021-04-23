import random


def make_character():
    """Create a character

    :postcondition: ask user for name
    :postcondtiion: create a dictionary with character information
    :return: the dictionary
    """
    name = input('Name: ')
    character = {
                 'name': name,
                 'type': 'student',
                 'x': 2,
                 'y': 2,
                 'credit': 0,
                 'stress': 0,
                 'iq': 100,
                 'surrendered': False
                 }
    return character


def print_character(character):
    """Print character

    :postcondition: print the character
    :return: None
    """
    print("----------------------------")
    for key, value in character.items():
        print(f"{key}: {value}")
    print("----------------------------")


def surrender(character: dict) -> None:
    """surrender

    :postcondition: change the character's surrendered value to true
    :return: None
    """
    character['surrendered'] = True


def flee(character_stat: dict) -> None:
    """Flee the scene

    :param character_stat: a dictionary
    :precondition: character_stat must be a dictionary
    :postcondition: At every 1/10 chance, instructor detects you fleeing
    :postcondition: Else, escape the scene successfully
    :return: None
    """
    if random.randint(1, 10) == 1:
        damage = random.randint(1, 50)
        character_stat['stress'] += damage
        print(f"Instructor had attacked you in the back by {damage} points.")
    else:
        print('you have successfully fled the scene.')
