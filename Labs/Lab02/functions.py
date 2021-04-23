# Functions.py covers #8, #9 of Lab02


def format_name(first_name, last_name):
    """
    Return the full_name

    :param first_name: a string
    :param last_name: a string
    :precondition: first_name must be a string
    :precondition: last_name must be a string
    :postcondition: remove white space and capitalize each string
    :postcondition: concatenate two string and a space in between
    :return: full name with title case
    """
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()
    return first_name + " " + last_name


def tripler(my_var):
    """
    Return string repeated three times

    :param my_var: a variable with value of float/int/string type
    :precondition: my_var must be a float/int/string type
    :postcondition: turn my_var to string
    :postcondition: repeat str(my_var) three times
    :return: the tripled argument
    """
    return str(my_var) * 3


def this_year():
    """
    Return the sun of two integer

    :postcondition: add two integers, turing_birthyear and turing_age_if_alive
    :return: the integer year
    """
    turing_birthyear = 1912
    turing_age_if_alive = 107
    year = turing_birthyear + turing_age_if_alive
    return year


def base_conversion():
    """
    return the number converted to specified base

    :postcondition: prompt user input of integer(2-9) for destination_base
    :postcondition: calculate the max_decimal_number given formula (destination_base**4 -1)
    :postcondition: prompt user input of integer(0~max_decimal_number)
    :postcondition: initiate the converted number variable by assigning an empty string
    :postcondition: using for loops, concatenate the resulting remainder while reassigning quotient to be a new decimal_number
    :postcondition: print the converted_number which has been converted to the integer
    :return: nothing
    """
    destination_base = int(input("Enter the destination base (2-9) and press enter : "))
    max_decimal_number = destination_base ** 4 - 1
    decimal_number = int(input("Enter a base ten number (0~%d): " % max_decimal_number))
    converted_number = ""
    for i in range(4):
        quotient = decimal_number // destination_base
        remainder = decimal_number % destination_base
        converted_number = str(remainder) + converted_number
        decimal_number = quotient
    print(int(converted_number))


def main():
    """Execute the program"""

    print(format_name("  DONGmin   ", " lEE"))

    print(tripler("Hello"))
    print(tripler(3))
    print(tripler(2.0))

    print(this_year())

    base_conversion()


if __name__ == "__main__":
    main()
