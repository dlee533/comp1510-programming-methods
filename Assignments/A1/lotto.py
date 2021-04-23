import random


def number_generator():
    """
    print the sorted 6 numbers in a list

    :postcondition: create an empty list
    :postcondition: call function get_numbers to get 6 random numbers(1~49)
    :postcondition: sort the list
    :postcondition: print the list
    :return: none
    """
    numbers = []
    print(sorted(get_numbers(numbers)))


def get_numbers(num_list):
    """
    append six random, non repeating numbers to the list

    :param num_list: an empty list
    :precondition: the list must be an empty one
    :postcondition: get a random number from 1 to 49
    :postcondition: append if the random number does not already exist in the list
    :postcondition: if the length of the list is 6, return the list
    :postcondition: after the complete execution of the if statement or if
                    statement results in a False, call itself.
    :return: the list
    """
    random_number = random.randint(1, 49)
    if random_number not in num_list:
        num_list.append(random_number)
        if len(num_list) == 6:
            return num_list
    return get_numbers(num_list)


def main():
    """execute the function : doctest cannot be written due to random module"""
    number_generator()


if __name__ == "__main__":
    main()
