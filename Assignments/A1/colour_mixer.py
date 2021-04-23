def colour_mixer():
    """
    print the result of two mixed colour

    :postcondition: prompt user to input colour_one, a primary colour
    :postcondition: prompt  user to input  colour_two, a different primary colour
    :postcondition: if two colours are identical, print error message
    :postcondition: print mixed colour if two colours are valid input
    :postcondition: print error message if the inputs were invalid
    :return: none
    """
    colour_one = input("Enter one primary colour (red/yellow/blue) : ")
    colour_two = input("Enter another primary colour (red/yellow/blue) : ")

    if colour_one == colour_two:
        print("Error. Two colours you have entered are identical.")
    elif colour_one == "red" or colour_two == "red":
        if colour_one == "yellow" or colour_two == "yellow":
            print("Orange")
        elif colour_one == "blue" or colour_two == "blue":
            print("Purple")
        else:
            print("You have entered invalid input.")
    elif colour_one == "yellow" or colour_two == "yellow":
        if colour_one == "blue" or colour_two == "blue":
            print("Green")
        else:
            print("You have entered invalid input.")
    else:
        print("You have entered invalid input.")


def main():
    """execute the colour mixer : this function requires user inputs, therefore cannot write doctest"""
    colour_mixer()

if __name__ == "__main__":
    main()