import math
import doctest
import sys


def eratosthenes(upperbound: int):
    """Return a list of primes between [0, upperbound]

    :param upperbound: a int
    :precondition: upperbound must be a positive integer
    :postcondition: if upperbound is not a positive integer, raise an error, print helpful message, and return None
    :postcondition: create a set with numbers from 2 to upperbound
    :postcondition: calculate a square root of the upper bound
    :postcondition: for number from 2 to sqrt of upper bound, check if the number's multiples are in the previous set
    and if it is put it in the new set
    :postcondition: subtract the newly made set from all_num
    :postcondition: change the type of all_num to list and return
    :return: list, all_num
    >>> eratosthenes(0)
    []
    >>> eratosthenes(-5)

    >>> eratosthenes(5)
    [2, 3, 5]
    """
    try:
        if upperbound < 0:
            raise ValueError("upperbound must be a positive integer")
        all_num = {i for i in range(2, upperbound+1)}
    except (TypeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
    else:
        sqrt_of_upperbound = math.ceil(math.sqrt(upperbound + 1))
        for i in range(2, sqrt_of_upperbound):
            multiples_of_i = {num for num in all_num if num % i == 0 and num // i > 1}
            all_num = all_num.difference(multiples_of_i)
        return list(all_num)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
