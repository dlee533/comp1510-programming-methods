import doctest


def number_translator():
    """
    print the translated number

    :postcondition: prompt the user to enter telephone number in the right format
    :postcondition: assign an empty string to number_output
    :postcondition: call the translate_digit function to translate each digit to numbers
    :postcondition: print the number_output
    :return: none
    """
    telephone_input = input("Enter the telephone number in the format XXX-XXX-XXXX : ").upper()
    number_output = ""
    number_output = translate_digit(telephone_input, number_output)

    print(number_output)


def translate_digit(telephone, converted):
    """
    return the translated digits
    
    :param telephone: a string
    :param converted: a string
    :precondition: telephone must be a string
    :precondition: converted must be a string, its length must be smaller
                    than the length of the telephone
    :postcondition: check if the digit is a number or a hyphen, if True,
                    append the same value to the converted
    :postcondition: check if the digit is an alphabet, depending on which,
                    append matching number to the converted
    :postcondition: if the length of the telephone is equal to the converted,
                    return the converted
    :postcondition: if the length of the telephone is not equal to the
                    len(converted), call itself again
    :return: the converted number
    
    >>> translate_digit("000-000-0000", "000-000-000")
    '000-000-0000'
    >>> translate_digit("555-GET-FOOD", "")
    '555-438-3663'
    >>> translate_digit("ABC-DEF-GHKZ","222")
    '222-333-4459'
    """
    if telephone[len(converted)] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"):
        converted += telephone[len(converted)]
    elif telephone[len(converted)] in ("A", "B", "C"):
        converted += "2"
    elif telephone[len(converted)] in ("D", "E", "F"):
        converted += "3"
    elif telephone[len(converted)] in ("G", "H", "I"):
        converted += "4"
    elif telephone[len(converted)] in ("J", "K", "L"):
        converted += "5"
    elif telephone[len(converted)] in ("M", "N", "O"):
        converted += "6"
    elif telephone[len(converted)] in ("P", "Q", "R", "S"):
        converted += "7"
    elif telephone[len(converted)] in ("T", "U", "V"):
        converted += "8"
    elif telephone[len(converted)] in ("W", "X", "Y", "Z"):
        converted += "9"

    if len(telephone) == len(converted):
        return converted

    return translate_digit(telephone, converted)
    

def main():
    """execute the doctest : number_translator() requires input, so doctest is
        only written on translate_digit"""
    doctest.testmod()


if __name__ == "__main__":
    main()
