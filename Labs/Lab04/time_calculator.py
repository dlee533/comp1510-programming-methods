import doctest


def time_calculator(seconds):
    """
    print the seconds converted to (days, hours, minutes and seconds)

    :param seconds: an integer
    :precondition: the seconds must an integer
    :postcondition: the seconds are converted to days, hours, minutes
    :postcondition: the result is printed using f string format
    :return: none

    >>> time_calculator(0)
    0 0 0 0
    >>> time_calculator(3600)
    0 1 0 0
    >>> time_calculator(50000)
    0 13 53 20
    """
    days, seconds = convert_to_unit(seconds, 86400)
    hours, seconds = convert_to_unit(seconds, 3600)
    minutes, seconds = convert_to_unit(seconds, 60)

    print(f"{days} {hours} {minutes} {seconds}")


def convert_to_unit(seconds, seconds_per_unit):
    """
    Return two integers that are the quotient and remainder of the division

    :param seconds: an integer
    :param seconds_per_unit: an integer
    :precondition: both should be a positive integer
    :postcondition: calculate the quotient and remainder of two numbers
    :return: return two numbers

    >>> convert_to_unit(1, 1)
    (1, 0)
    >>> convert_to_unit(0, 60)
    (0, 0)
    >>> convert_to_unit(500, 60)
    (8, 20)
    """
    return seconds//seconds_per_unit, seconds % seconds_per_unit


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
