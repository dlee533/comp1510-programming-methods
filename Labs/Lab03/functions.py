import random, doctest


def roll_die(number_of_rolls, number_of_sides):
    """
    Return the sum of the die results

    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: number_of rolls and number_of_sides must be a positive int
    :precondition: number_of_rolls must be 3 or smaller
    :postcondition: if the preconditions are not met, return 0
    :postcondition: calculate the possible sum one can get from rolling the die value of "number_of_rolls
                    times
    :postcondition: get a random integer between min(number of rolls) max(num of rolls* num of sides)
    :return: the sum of die results
    """
    if type(number_of_rolls) == int and type(number_of_sides) == int:
        if number_of_rolls > 0 and number_of_sides > 0:
            return random.randint(number_of_rolls, number_of_rolls*number_of_sides)
    return 0


def create_name(length):
    """
    return the generated name

    :param length: an integer
    :precondition: has to be a positive integer, if not, None is returned
    :postcondition: assign an empty string to the variable"name"
    :postcondition: concatenate a randomly generated letter(through add_a_letter function)
                    the length times
    :return: name with length of the argument, length/None if the precondition is not met
    """
    name = ""
    if type(length)!=int or length < 0:
        return None
    if length >= 1:
        name += add_a_letter()
    if length >= 2:
        name += add_a_letter()
    if length >= 3:
        name += add_a_letter()
    if length >= 4:
        name += add_a_letter()
    if length >= 5:
        name += add_a_letter()
    return name


def add_a_letter():
    """
    return a random alphabet

    :postcondition: randomly draw out an alphabet using choice function of random module
    :return: randomly generated letter
    """
    return random.choice("abcdefghijklmnopqrstuvwxyz")

def main():
    """doctest"""
    doctest.testmod()

if __name__ == "__main__":
    main()
