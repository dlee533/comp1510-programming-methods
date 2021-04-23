import sys
import doctest


def selection_sort(my_list: list) -> list:
    """sort the list

    :param my_list: a list
    :precondition: my_list must be a non-empty list with sortable items
    :postcondition: check the list length
    :postcondition: for each item in list, search the list linearly from the next item to the end for the item with
    least value, if found, assign the value and index to variables
    :postcondition: if the items are of unsortable types, throw an error
    :postcondition: swap the lowest value with the item of current index
    :return: None
    >>> selection_sort([1])
    [1]
    >>> selection_sort([3, 2, 1])
    [1, 2, 3]
    >>> selection_sort(['a', 'c', 'b'])
    ['a', 'b', 'c']
    """
    check_list_length(item_list=my_list)
    for i, element in enumerate(my_list):
        lowest_value = element
        lowest_index = i
        for j in range(i+1, len(my_list)):
            try:
                if my_list[j] < lowest_value:
                    lowest_value, lowest_index = my_list[j], j
            except TypeError as e:
                print(f"Error: {e}", file=sys.stderr)
                return None
        my_list[i], my_list[lowest_index] = my_list[lowest_index], my_list[i]
    return my_list


def check_list_length(item_list: list) -> None:
    """throw an enrror if the list is empty

    :param item_list: a list
    :precondition: item_list must be a list
    :postcondition: throw an error if the length of the item_list is zero
    :return: None
    >>> check_list_length([1, 2, 3])

    >>> check_list_length([])

    """
    try:
        if len(item_list) == 0:
            raise ValueError("the list cannot be empty")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
    else:
        return None


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()

