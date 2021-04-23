import doctest
import sys


def cash_money(value):
    """Breakdown money

    :param value: a float
    :precondition: value must be a positive float
    :postcondition: if the value is not a positive float, raise an error
    :postcondition: for each existing face value, if the value is equal or greater than it, add key value
    pair which represents the number of appropriate bill and subtract the matching number of dollars from
    the value
    :return: the dictionary, bill
    >>> cash_money(0)
    {}
    >>> cash_money(100)
    {100: 1}
    >>> cash_money(188.41)
    {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1, 0.25: 1, 0.1: 1, 0.05: 1, 0.01: 1}
    """
    try:
        if value < 0:
            raise ValueError
        elif type(value) == str:
            raise TypeError
    except (ValueError, TypeError):
        print(f"Error: the value must be a positive floating point", file=sys.stderr)
        return None
    else:
        denominations = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
        bill = {}
        for denomination in denominations:
            if value >= denomination:
                bill[denomination] = int(value//denomination)
                value -= bill[denomination] * denomination
                value = round(value, 2)
        return bill


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()

