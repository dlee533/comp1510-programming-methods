import doctest


def gcd(a: int, b: int) -> int:
    """Divide until remainder is zero

    :param a: an integer
    :param b: an integer
    :precondition: a must be an integer
    :precondition: b must be an integer
    :postcondition: if b/remainder from previous division is zero, return a
    :postcondition: calculate the remainder from division of a and b
    :postcondition: call itself with b and remainder as arguments
    :return: b, integer
    >>> gcd(0, 0)
    0
    >>> gcd(3, 9)
    3
    >>> gcd(9, 3)
    3
    """
    if b == 0:
        return abs(a)
    remainder = a % b
    return gcd(b, remainder)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
