import doctest
import sys


def gcd(a: int, b: int, initial_input: bool = True) -> int:
    """Divide until remainder is zero

    :param initial_input:
    :param a: an integer
    :param b: a boolean
    :precondition: a must be an integer
    :precondition: b must be an integer
    :precondition: initial_input is a boolean value, if nothing is passed, its default value is True
    :precondition: if a and b are not non zero integers, raise an error
    :postcondition: if b/remainder from previous division is zero, return a
    :postcondition: calculate the remainder from division of a and b
    :postcondition: call itself with b and remainder as arguments
    :return: b, integer
    >>> gcd(0, 0)

    >>> gcd(3, 9)
    3
    >>> gcd(9, 3)
    3
    """
    if initial_input:
        try:
            if a == 0 or b == 0:
                raise ValueError('a and b must be non zero')
            if a % 1 != 0 or b % 1 != 0:
                raise TypeError('a and b must be integers')
        except (ValueError, TypeError) as e:
            print(f"Error: {e}", file=sys.stderr)
            return None
    if b == 0:
        return abs(a)
    remainder = a % b
    return gcd(a=b, b=remainder, initial_input=False)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
