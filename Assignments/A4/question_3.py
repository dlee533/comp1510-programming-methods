import doctest


def dijkstra(colour_list: list) -> None:
    """sort the list

    :param colour_list: a list
    :precondition: cololur_list must be a list with any number of 'red', 'white', and 'blue'
    :postcondition: sort the list with value returned from second_character function
    :return: None
    """
    colour_list.sort(key=second_character)


def second_character(word: str) -> str:
    """Return the second character

    :param word: a string
    :precondition: word must be a string
    :return: the second character/index one of the string
    >>> second_character('white')
    'h'
    >>> second_character('red')
    'e'
    >>> second_character('blue')
    'l'
    """
    return word[1]


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
