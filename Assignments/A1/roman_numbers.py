import doctest


def convert_to_roman_numeral(positive_int):
    """
    Return the Roman numeral which is equivalent to the positive_int input

    :param positive_int: an integer
    :precondition: must be a positive integer in range [1~10,000]
    :postcondition: set variable, roman_numeral to empty string
    :postconditioin: process positive_int and reassign new values to roman_numeral and positive_int
    :return:  the roman_numeral which is equivalent

    >>> convert_to_roman_numeral(1)
    'I'
    >>> convert_to_roman_numeral(499)
    'CDXCIX'
    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    """
    roman_numeral = ""

    roman_numeral, positive_int = divide_by_base(positive_int, 1000, roman_numeral, "M")
    roman_numeral, positive_int = divide_by_base(positive_int, 900, roman_numeral, "CM")
    roman_numeral, positive_int = divide_by_base(positive_int, 500, roman_numeral, "D")
    roman_numeral, positive_int = divide_by_base(positive_int, 400, roman_numeral, "CD")
    roman_numeral, positive_int = divide_by_base(positive_int, 100, roman_numeral, "C")
    roman_numeral, positive_int = divide_by_base(positive_int, 90, roman_numeral, "XC")
    roman_numeral, positive_int = divide_by_base(positive_int, 50, roman_numeral, "L")
    roman_numeral, positive_int = divide_by_base(positive_int, 40, roman_numeral, "XL")
    roman_numeral, positive_int = divide_by_base(positive_int, 10, roman_numeral, "X")
    roman_numeral, positive_int = divide_by_base(positive_int, 9, roman_numeral, "IX")
    roman_numeral, positive_int = divide_by_base(positive_int, 5, roman_numeral, "V")
    roman_numeral, positive_int = divide_by_base(positive_int, 4, roman_numeral, "IV")
    roman_numeral, positive_int = divide_by_base(positive_int, 1, roman_numeral, "I")

    return roman_numeral


def divide_by_base(number, roman_base_number, roman_string, roman_base_letter):
    """
    return the new roman_string and number

    :param roman_base_letter:
    :param number: a positive integer
    :param roman_base_number: a positive integer
    :param roman_string: a string
    :param roman_base_letter: a string
    :precondition: number and roman_base must be a positive integer
    :precondition: roman_base_number must be one of [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    :precondition: roman_string and roman_base_letter must be strings
    :postcondition: assess if quotient of number//roman_base is greater than 0
    :postcondition: reassign the roman_string and number
    :return: reassigned or original roman_string and number based on the postcondition

    >>> divide_by_base(1, 1, "", "I")
    ('I', 0)
    >>> divide_by_base(12, 10, "M", "X")
    ('MX', 2)
    >>> divide_by_base(357, 100, "", "C")
    ('CCC', 57)
    """
    if number//roman_base_number > 0:
        return roman_string + roman_base_letter * (number//roman_base_number), \
               number % roman_base_number
    return roman_string, number


def main():
    """doctest"""
    doctest.testmod()


if __name__ == "__main__":
    main()
