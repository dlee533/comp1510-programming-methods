import doctest


def time_calculator(seconds):
    """
    print the seconds converted to (days, hours, minutes and seconds)

    :param seconds: an integer
    :precondition: the seconds must an integer
    :postcondition: the seconds are converted to days, hours, minutes and remaining seconds by
                    calculating the quotient of division
    :postcondition: the result is printed using f string format
    :return: none

    >>> time_calculator(0)
    0 0 0 0
    >>> time_calculator(3600)
    0 1 0 0
    >>> time_calculator(50000)
    0 13 53 20
    """
    days = seconds//86400
    seconds %= 86400
    hours = seconds//3600
    seconds %= 3600
    minutes = seconds//60
    seconds %= 60

    print(f"{days} {hours} {minutes} {seconds}")


def main():
    doctest.testmod()

if __name__ == "__main__":
    main()