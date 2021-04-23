"""
- the dictionary doesn't include the index of zero, if there are any trailing zeros,
after the highest key (index) it won't be displayed on dictionary
- full length of sparsevector and whether their full length, including the zeroes are the same
"""

import doctest


def sparse_add(dict_one, dict_two):
    """Return the sparsed dictionary

    :param dict_one: a dictionary
    :param dict_two: a dictionary
    :precondition: dict_one and dict_two must be dictionaries
    :postcondition: append the key value pair of dict_one to temp_dict
    :postcondition: if the key of dict_two already exist in temp_dict, add the value, if not, add the key value pair
    to the dictionary
            temp_dict[index] = dict_two[index
    :postcondition: for all pairs in temp_dict, if the values are not zero, add the pair to the final dictionary
    :return: final dictionary
    >>> sparse_add({}, {})
    {}
    >>> sparse_add({1: 4}, {2: 5})
    {1: 4, 2: 5}
    >>> sparse_add({1: 2},{1: 2})
    {1: 4}
    """
    temp_dict = {key: value for key, value in dict_one.items()}
    dict_output = {}
    for index in dict_two:
        if index not in temp_dict:
            temp_dict[index] = dict_two[index]
        else:
            temp_dict[index] += dict_two[index]
    for index in temp_dict:
        if temp_dict[index] != 0:
            dict_output[index] = temp_dict[index]
    return dict_output


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
