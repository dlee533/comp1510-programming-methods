import random
import doctest


def CLASSES():
    """return the constant dictionary

    :return: class dictionary
    >>> CLASSES()
    {'barbarian': 12, 'bard': 8, 'cleric': 8, 'druid': 8, 'fighter': 10, 'monk': 8, 'paladin': 10, 'ranger': 10, 'rogue': 8, 'sorcerer': 6, 'warlock': 8, 'wizard': 6}
    """
    return {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8, "fighter": 10,
            "monk": 8, "paladin": 10, "ranger": 10, "rogue": 8, "sorcerer": 6,
            "warlock": 8, "wizard": 6}


def roll_die(number_of_rolls, number_of_sides):
    """Return the sum of die rolls

    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: number_of_rolls and number_of sides must be integers
    :postcondition: initialize the variable total
    :postcondition: for number_of_rolls times, roll the die of number_of_sides sides and increment the total
    :return: total
    """
    total = 0
    if number_of_sides > 0 and number_of_rolls > 0:
        for i in range(number_of_rolls):
            total += random.randint(1, number_of_sides)
    return total


def display_item(item_list):
    """Print the list

    :param item_list: a list
    :precondition: item_list must be a list
    :postcondition: set counter
    :postcondition: for every element, print the counter and the element
    :return: no return
    >>> display_item([])
    Here is what we have for sale:
    >>> display_item(['One'])
    Here is what we have for sale:
    1. One
    >>> display_item(['One', 'Two'])
    Here is what we have for sale:
    1. One
    2. Two
    """
    print("Here is what we have for sale:")
    count = 1
    for element in item_list:
        print(f"{count}. {element}")
        count += 1


def add_item_to_list(item_list):
    """Return the user input

    :param item_list: a list
    :precondition: item_list must be a list
    :postcondition: display item_list
    :postcondition: prompt the user to input a number
    :postcondition: if the user input meets the condition, return it with boolean True
    :postconditioin: if the user input is -1, return None with boolean False
    :postcondition: else, call the function again
    :return: the num or None
    """
    display_item(item_list)
    user_choice = input("What would you like to buy (-1 to finish) ").strip()
    if user_choice.isdigit() and 1<=int(user_choice)<=len(item_list):
        return int(user_choice)
    elif user_choice == '-1':
        return None
    print("Invalid choice. Please enter the number corresponding to the choices listed.")
    return add_item_to_list(item_list)


def choose_inventory(inventory):
    """Return the temporary item list

    :param inventory: a list
    :precondition: inventory must be a list
    :postcondition: initialize temp_item_list
    :postcondition: get user choice and if it meets the condition, append to the list, if None is returned
    quit the while loop
    :return: temporary item list
    """
    print("Welcome to the Olde Tyme Merchant!")
    temp_item_list = []
    choice = "initializing the variable"
    while choice:
        choice = add_item_to_list(inventory)
        if choice:
            temp_item_list.append(inventory[choice-1])
    return temp_item_list


def generate_consonant():
    """Return a consonant

    :postcondition: randomly choose a consonant
    :return: consonant
    """
    return random.choice("bcdfghjklmnpqrstvwxyz")


def generate_syllable():
    """Return a syllable

    :postcondition: concatenate the randomly generated consonant and vowel in that order
    :return: concatenated letter, the syllable
    """
    return generate_consonant() + generate_vowel()


def generate_vowel():
    """Return a vowel

    :postcondition: randomly choose a vowel
    :return: vowel
    """
    return random.choice("aeiouy")


def generate_name(syllables):
    """Return the generated name

    :param syllables: an integer
    :precondition: syllables must be an integer
    :postcondition: initialize the name variable
    :postcondition: for the syllable times, concatenate a randomly generated syllable
    :return: capitalized name
    """
    name = ""
    for i in range(syllables):
        name += generate_syllable()
    return name.capitalize()


def display_without_number(data_structure):
    """Print the data structure

    :param data_structure: a list or a dictionary
    :precondition: data_structure must be a list or a dictionary
    :postcondition: for element in data_structure, print the element
    :return: no return statement
    >>> display_without_number([])

    >>> display_without_number([1, 2, 3])
    - 1
    - 2
    - 3
    >>> display_without_number({1: 2, 3: 4})
    - 1
    - 3
    """
    for element in data_structure:
        print(f"- {element}")


def select_class():
    """return the string, class

    :postcondition: call CLASSES() function to get the class dictionary
    :postcondition: display the classes
    :postcondition: prompt user to enter a class
    :postcondition: if the user input is in the class, return the class
    :postcondition: else, print the message and call the select_class function again
    :return: the user input
    """
    class_dict = CLASSES()
    display_without_number(class_dict)
    user_input = input("Choose a class ").lower().strip()
    if user_input in class_dict:
        return user_input, class_dict[user_input]
    print("Invalid input.")
    return select_class()


def select_race():
    """return the user input

    :postcondition: assign a list to race_list
    :postcondition: display the race_list
    :postcondition: prompt the user to enter a race
    :postcondition: if the user input is in the race_list, return the user input
    :postcondition: else, display a message and call the select_race function again
    :return: user input
    """
    race_list = ["dragonborn", "dwarf", "elf", "gnome", "half-elf", "halfling", "half-orc", "human",
                 "tiefling", "aarakocra", "genasi", "goliath", "aasimar", "bugbear", "firbolg", "goblin",
                 "hobgoblin", "kenku", "kobold", "lizardfolk", "orc", "tabaxi", "triton", "yuan-ti pureblood",
                 "feral tielfling", "tortle", "gith", "changeling", "kalashtar", "shifter", "warforged",
                 "centaur", "loxodon", "minotaur", "simic hybrid", "vedalken", "verdan", "locathah"]
    display_without_number(race_list)
    user_input = input("Choose a class from following ").lower().strip()
    if user_input in race_list:
        return user_input.capitalize()
    print("Invalid input.")
    return select_race()


def create_character(name_length):
    """Return a dictionary about a character's detail

    :param name_length: an integer
    :precondition: name_length must be an integer
    :postcondition: call and assign class name and die sides
    :postcondition: get hp
    :postcondition: concatenate key value pairs
    :return: the character dictionary
    """
    class_name, die_sides = select_class()
    hp = roll_die(1, die_sides)
    character = {"Name": generate_name(name_length),
                 "Race": select_race(),
                 "Class": class_name,
                 "HP": [hp, hp]}
    attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for attribute in attributes:
        character[attribute] = roll_die(3, 6)
    character["XP"] = 0
    character["Inventory"] = []
    return character


def print_character(character):
    """Print the character dictionary

    :param character: a dictionary
    :precondition: character must be a formatted dictionary
    :postcondition: if the key is not equal to "HP" or "Inventory, print the key value pair in one format
    :postcondition: elif the key is equal to "HP", print the key value pair in another format
    :postcondition: elif the key is equal to "Inventory", print the key value pair in yet another format

    >>> print_character({"Name" : "Mike"})
    --------------------------------
    Character Details
    Name : Mike
    --------------------------------
    >>> print_character({"Name" : "Mike", "HP" : [10,10]})
    --------------------------------
    Character Details
    Name : Mike
    HP : 10/10
    --------------------------------
    >>> print_character({'Name': 'Mike', 'HP': [10, 10], 'Inventory': ['Sword']})
    --------------------------------
    Character Details
    Name : Mike
    HP : 10/10
    Inventory : <Sword>
    --------------------------------
    """
    print("--------------------------------")
    print("Character Details")
    for attribute, value in character.items():
        if attribute != "HP" and attribute != "Inventory":
            print(f"{attribute} : {value}")
        elif attribute == "HP":
            print(f"{attribute} : {value[1]}/{value[0]}")
        elif attribute == "Inventory":
            print("Inventory :", end="")
            for item in character[attribute]:
                print(f" <{item}>", end="")
            print()
    print("--------------------------------")


def inflict_damage(attacker_name, defender_dictionary):
    """Return the defender_dictionary

    :param attacker_name: a string
    :param defender_dictionary: a dictionary
    :precondition: attacker_name and defender_dictionary must be said types
    :postcondition: get damage by rolling a die of sides from class dictionary
    :postcondition: display usefull message
    :postcondition: if the damage is equal or greater than the hp, set hp to 0
    :postcondition: else, subtract the damage amount from the hp
    :return: the defender dictionary
    """
    damage = roll_die(1, CLASSES()[defender_dictionary["Class"]])
    print(f"{attacker_name} had successfully attacked "
          f"{defender_dictionary['Name']} by {damage} HP.")
    if defender_dictionary["HP"][1] <= damage:
        print(f"{defender_dictionary['Name']} died.")
        defender_dictionary["HP"][1] = 0
    else:
        defender_dictionary["HP"][1] -= damage
        print(f"{defender_dictionary['Name']}'s current HP is {defender_dictionary['HP'][1]}.")
    return defender_dictionary


def attack_succeeded(defender_dexterity):
    """return boolean value, depending on the random die roll

    :param defender_dexterity: an integer
    :precondition: defender_dexterity must be an integer
    :postcondition: roll the die 1d20, and if the resulting value is bigger, return True
    :postcondition: else, False
    :return: boolean value
    """
    if roll_die(1, 20) > defender_dexterity:
        return True
    else:
        return False


def attempt_attack(attacker, defender):
    """return the defender dictionary

    :param attacker: a dictionary
    :param defender: a dictionary
    :precondition: both parameter must be a formatted dictionary
    :postcondition: print whose turn it is to attack
    :postcondition: if the attacker succeeds at attacing, inflict the damage by calling different functions
    :postcondition: else, prints helpful message
    :return: defender dictionary
    """
    print(f"{attacker['Name']}'s turn to attack...")
    if attack_succeeded(defender['Dexterity']):
        defender = inflict_damage(attacker['Name'], defender)
    else:
        print("Attack failed.")
    return defender


def decide_turn():
    """return number depending on value returned from other function

    :postcondition: roll die twice
    :postcondition: if two rolls result in same numbers, roll agaub
    :postcondition: else, return 0 or 1 depending on which number is greater
    :return: 0 or 1
    """
    while True:
        roll_one = roll_die(1, 20)
        roll_two = roll_die(1, 20)
        if roll_one != roll_two:
            return 0 if roll_one > roll_two else 1


def combat_round(opponent_one, opponent_two):
    """return two dictionaries

    :param opponent_one: a dictionary
    :param opponent_two: a dictionary
    :precondition: bothe opponents must be a dictionary
    :postcondition: store two dicts in a list
    :postcondition: decide turn
    :postcondition: first turn attack the second and the second's dict may change
    :postcondition: if the second turn did not die, the second turn attacks the first
    :postcondition: second attack the first, and the dicionary value may change
    :return: Nothing
    """
    characters = [opponent_one, opponent_two]

    character_index = decide_turn()
    first_turn = characters[character_index]
    second_turn = characters[1-character_index]

    second_turn = attempt_attack(first_turn, second_turn)
    if second_turn['HP'][1] > 0:
        first_turn = attempt_attack(second_turn, first_turn)



def main():
    """Execute the functions and docstring"""
    print("The character name is generated by using user input and attribute values from the result of "
          "die roll\n")

    print(f"Each syllable is generated by using generate_syllable() (ex. '{generate_syllable()}' returned)")
    print("And each syllable is generated by using generate_consonant() and generate_vowel() "
          f"(ex. '{generate_consonant()}', '{generate_vowel()}' returned)\n")

    num_syllable = int(input("For the complete name, user must input a number of syllable: "))
    print(f"The generated name is {generate_name(num_syllable)}.\n")

    print("Then the die is rolled for attributes (HP, Strength, Dexterity, Constitution, Intelligence, Wisdom,"
          " Charisma).")
    num_roll, num_sides = input("Enter two integers, number of rolls and number of sides, with a space "
                                "in between: ").strip().split(" ")
    print(f"You've got the total sum of {roll_die(int(num_roll), int(num_sides))} from {num_roll} roll with "
          f"{num_sides} sided die\n")

    input("Now that you know the basic functions, press enter to start the tutorial")
    print()

    character_list = []
    items = ["Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"]
    for i in range(2):
        syllable = int(input(f"How many syllables for the name of charcter {i+1}? "))
        character_list.append(create_character(syllable))
        print()
        character_list[i]["Inventory"] = choose_inventory(items)
        print()

    print("Following is the information generated by previous inputs:")
    for j in range(2):
        print_character(character_list[j])
    print()

    input("Press Enter to start a round of combat.")
    combat_round(character_list[0], character_list[1])
    print()

    input("Press Enter to display the final character detail.")
    for j in range(2):
        print_character(character_list[j])

    doctest.testmod()


if __name__ == "__main__":
    main()
