import doctest
import random


def list_tagger(batch):
    """Tag list with length

    :param batch: a list
    :precondition: batch must be a list
    :postcondition: determine the length of the list
    :postcondition: insert the length as an integer into the list at the beginning of the list
    :return: the list
    >>> list_tagger([1,2,3])
    [3, 1, 2, 3]
    >>> list_tagger(['a'])
    [1, 'a']
    >>> list_tagger([])
    [0]
    """
    length = len(batch)
    batch.insert(0, length)
    return batch


def cutoff(int_list, my_int):
    """Count the number of integers in the list that are multiple of the given number number

    :param int_list: a list
    :param my_int: an integer
    :precondition: int_list must be list of integers
    :precondition: my_int must be an integer
    :postcondition: initiate a counter
    :postcondition: for every element in a list, if the integer is a multiple of the given number increment
    the count
    :return: count
    >>> cutoff([1, 2, 3], 1)
    3
    >>> cutoff([], 1)
    0
    >>> cutoff([1, 2, 3], 3)
    1
    """
    count = 0
    for integer in int_list:
        if integer % my_int == 0:
            count += 1
    return count


def prepender(str_list, my_str):
    """Prepend the given string to each string in the list

    :param str_list: a list
    :param my_str: a string
    :precondition: str_list must be a list of strings
    :precondition: my_str must be a string
    :postcondition: for each element in the list, prepend the given string to the beginning of each
    string in the given list
    :return: None
    """
    for i in range(len(str_list)):
        str_list[i] = my_str + str_list[i]


def name_list():
    """Create a dicitonary with length of the name as key and name input by user in dictionary data structure
    as value

    :postcondition: initialize the dicitonary
    :postcondition: while user doesn't type in quit, prompt the user to enter a name
    :postcondition: if the length of the name doesn't exist in the dictionary as a key, create a key with
    the name list inside the dictionary as the value
    :postcondition: if the length of the name exist in the dictionary as a key, append the name to the list
    matching the length of the name
    :return: dictionary
    """
    name_dict = {}
    while True:
        user_input = input("Enter a name(type 'quit' to quit): ")
        if user_input == "quit":
            break
        elif len(user_input) in name_dict:
            name_dict[len(user_input)].append(user_input)
        else:
            name_dict[len(user_input)] = [user_input]
    return name_dict


def multiples_of_3(upper_bound):
    """Get the sum of all the positive multiples of 3 below upper_bound

    :param upper_bound: an integer
    :precondition: upper_bound must be an integer
    :postcondition: initate sum
    :postcondition: add the multiples of 3 below upper_bound to sum
    :return: sum
    >>> multiples_of_3(-3)
    0
    >>> multiples_of_3(0)
    0
    >>> multiples_of_3(10)
    18
    """
    total = 0
    for num in range(3, upper_bound, 3):
        total += num
    return total


def roll_a_die():
    """Print the simulated die result

    :postcondition: prompt the user to enter sides of a die and number of rolls to simulate
    :postcondition: create a dictionary with its keys reflecting the sides of a die and value 0
    :postcondition: until there is no more rolls left, get a random die roll, increment the value of
    matching key by one, and decrement the rolls by one
    :postcondition: print each key, value pairs
    :return: None
    """
    sides = int(input("Enter the sides of a die: "))
    rolls = int(input("Enter the number of rolls: "))
    result = {i: 0 for i in range(1, sides+1)}
    while rolls > 0:
        die_roll = random.randint(1, sides)
        result[die_roll] += 1
        rolls -= 1
    for key, value in result.items():
        print(f"{key} was rolled {value} times.")


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
