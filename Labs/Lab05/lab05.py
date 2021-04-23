import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """Return the sum of die rolls

    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: number_of_rolls and number_of_sides must be integers
    :postcondition: initialize sum
    :postcondition: if the parameters are not positive integers, return 0
    :postcondition: for number of rolls, add the random die roll
    :return: the sum of die rolls
    """
    total = 0
    if number_of_sides > 0 and number_of_rolls > 0:
        for i in range(number_of_rolls):
            total += random.randint(1, number_of_sides)
    return total


def choose_inventory(inventory, selection):
    """return the list of items

    :param inventory: a list
    :param selection: an integer
    :precondition: inventory must be a list, and selection an integer
    :postcondition: if the selection is negative, output an error message
    :postcondition: if the selection is equal to the length of inventory, copy the inventory list to
                    to the item_list
    :postcondition: if the selection is greater than the length of the inventory print the error message
                    and copy the inventory list to the item_list
    :postcondition: else, concatenate the random item selection times to the item_list
    :return: the item_list
    """
    item_list = []
    if selection < 0:
        print("Error! Selection cannot be a negative number.")
    elif len(inventory) == 0:
        print("Error! Inventory is empty.")
    elif selection == len(inventory):
        item_list = sorted(inventory)
    elif selection > len(inventory):
        print("Error! Selection cannot be greater than the length of inventory.")
        item_list = sorted(inventory)
    else:
        for i in range(selection):
            item_list.append(random.choice(inventory))
    return item_list


def generate_name(syllables):
    """Return the generated string

    :param syllables: an integer
    :precondition: syllables must be an integer
    :postcondition: create an empty string name
    :postcondition: for syllable times, concatenate generated syllable
    :postcondition: capitalize the name
    :return: the randomly generated name
    """
    name = ""
    for i in range(syllables):
        name += generate_syllable()
    return name.capitalize()


def generate_vowel():
    """Return a random vowel

    :postcondition: select a random vowel
    :return: the randomly selected vowel
    """
    return random.choice("aeiouy")


def generate_consonant():
    """Return a random consonant

    :postcondition: select a random consonant
    :return: the randomly selected vowel
    """
    return random.choice("bcdfghjklmnpqrstvwxyz")


def generate_syllable():
    """Return the concatenated string

    :postcondition: concatenated consonant and vowel
    :return: the concatenated string
    """
    return generate_consonant() + generate_vowel()


def create_character(name_length):
    """Return the list of character description

    :param name_length: an integer
    :precondition: name_length must be a positive integer
    :postcondition: create a character list with one element, name in it
    :postcondition: create a list, attributes, with name of attributes
    :postcondition: for each attribute, append the attribute name and a random number to the
                    character list
    :return: the character list
    """
    character = [generate_name(name_length)]
    attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for attribute in attributes:
        character.append([attribute, roll_die(3, 6)])
    return character


def print_character(character):
    """Print the character list

    :postcondition: print the title of the list
    :postcondition: print the name
    :postcondition: for each attributes, print the formatted minilist
    :postcondition: if there's items minilist in the list, print it using specialized format

    >>> print_character(['Caliku', ['Strength', 7], ['Dexterity', 12]])
    Character Stats
    Name : Caliku
    Strength : 7
    Dexterity : 12
    >>> print_character(['Bilyba', ['Strength', 500], ['Dexterity', 0]])
    Character Stats
    Name : Bilyba
    Strength : 500
    Dexterity : 0
    >>> print_character(['My_name', ['Attribute_1', 71], ["Items", "Sword", "Rock"]])
    Character Stats
    Name : My_name
    Attribute_1 : 71
    Items : <Sword> <Rock>
    """
    print("Character Stats")
    print("Name : " + character[0])
    for i in range(1, len(character)):
        if character[i][0] != "Items":
            print(character[i][0], ":", character[i][1])
        else:
            print(character[i][0], end=" :")
            for j in range(1, len(character[i])):
                print(" <" + character[i][j] + ">", end="")
            print()


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
