import doctest

def base_conversion():
    """
   print the string_output converted to integer

   :postcondition: prompt the user to enter the base number 2~9
   :postcondition: calculate the max_decimal
   :postcondition: prompt the user to enter the positive decimal number below the max_decimal
   :postcondition: run the destination_number and decimal through the function divide_four_times
   :postcondition: convert the string to integer and then print
    """
    destination_base = int(input("Enter the destination base (2-9) and press enter : "))
    max_decimal = destination_base ** 4 - 1
    decimal = int(input("Enter a base ten number (0~%d): " % max_decimal))
    string_output = ""
    string_output = decimal_to_base(destination_base, decimal, string_output)
    print(int(string_output))


def decimal_to_base(base, number, output):
    """
    return the concatenated output

    :param base: an integer
    :param number: an integer
    :param output: a string
    :precondition: base and number must be integers and output a string
    :postcondition: concatenate the modulus of two numbers to output
    :postcondition: reassign the number to the quotient of the two numbers
    :postcondition: if number == 0, terminate the resursion
    :postcondition: if number is greater than zero, call itself again using reassigned number and output
    :return: the concatenated output
    >>> decimal_to_base(2,1,"")
    '1'
    >>> decimal_to_base(3,5,"125")
    '12125'
    >>> decimal_to_base(9,1,"81")
    '181'
    """
    output = str(number%base) + output
    number = number//base
    if number == 0:
        return output
    return decimal_to_base(base, number, output)


def main():
    """doctest"""
    doctest.testmod()


if __name__ == "__main__":
    main()