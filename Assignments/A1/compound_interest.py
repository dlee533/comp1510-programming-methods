import doctest


def compound_interest(P, r, n, t):
    """
    return the calculated balance after a certain number of years of compound interest
    
    :param P: principal amount that was originally deposited into the account, a float
    :param r: annual interest rate, a float
    :param n: number of times per year that the interest is compounded, an integer
    :param t: specified number of years, a float
    :precondition: each parameter must be in type that are specified above
    :postcondition: calculate the balance with given formula
    :return: the balance after a specified number of years of compound interest

    >>> compound_interest(0.00, 0.02, 1, 5)
    0.0
    >>> compound_interest(1000.00, .05, 12, 10)
    1647.01
    >>> compound_interest(50000.00, .15, 12, 25)
    2077206.01
    """
    return round(P*((1+(r/n))**(n*t)), 2)


def main():
    """doctest"""
    doctest.testmod()


if __name__ == "__main__":
    main()
