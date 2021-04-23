import random

def rock_paper_scissors():
    """
    print the result of the game

    :postcondition: get computer choice
    :postcondition: prompt the user for input
    :postcondition: if the user choice is invalid, print error message
    :postcondition: print out the computer choice
    :postcondition: print out the result of the game depending on user
                    input and computer choice
    :return: none
    """
    computer_choice = choose_computer()

    user_choice = input("Enter one of following (rock, paper, scissors) : ").strip().capitalize()

    if user_choice!="Rock" and user_choice!="Paper" and user_choice!="Scissors":
        print("It is an invalid input")
    else:
        print(f"Computer chose {computer_choice}.")
        if user_choice == computer_choice:
            print("It's a tie")
        elif user_choice == "Rock":
            if computer_choice == "Paper":
                print("You lose")
            else:
                print("You win")
        elif user_choice == "Paper":
            if computer_choice == "Rock":
                print("You win")
            else:
                print("You lose")
        else:
            if computer_choice =="Rock":
                print("You lose")
            else:
                print("You win")


def choose_computer():
    """
    return random choice from (rock, paper, scissor)

    :postcondition: assign a random number (0~2) to random number
    :postcondition: depending on the value of random number, assign
                    a string to computer_choice
    :return: the random choice (rock, paper, scissor)
    """
    random_number = random.randint(0,2)
    if random_number == 0:
        return "Rock"
    elif random_number == 1:
        return "Paper"
    else:
        return "Scissors"


def main():
    """execute the function : no doctest as the function contains user
        input and random module"""
    rock_paper_scissors()

if __name__ == "__main__":
    main()