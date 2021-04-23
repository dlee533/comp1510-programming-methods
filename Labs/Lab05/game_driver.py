from Lab05 import lab05


def main():
    print("Generate consonant/Generate vowel function works the following way...")
    print("Consonant : ", lab05.generate_consonant())
    print("Vowel : ", lab05.generate_vowel())
    print("The returned consonant and vowel then concatenates to form a single syllable. Like so..")
    print(lab05.generate_syllable())
    print("The returned syllable then concatenates to form a single name of the length of your choice.")
    syllables = int(input("Enter the number of syllables you want your name to be: "))
    print("Name: ", lab05.generate_name(syllables))

    print("__________________________________________________________________________________________________")

    print("Then the choose inventory function accepts two arguments, one with inventory list and the other\n"
          "number of items purchased. Say there are items list of acid, arrows, battleaxe, blowgun, book, \n"
          "crossbow, crowbar in the inventory.")
    inventory = ["acid", "arrows", "battleaxe", "blowgun", "book", "crossbow", "crowbar"]
    item_number = int(input("How many items wold you like to purchase? "))
    items = lab05.choose_inventory(inventory, item_number)
    print("You have", end=" ")
    for item in items:
        print("<" + item + ">", end=" ")
    print()

    print("__________________________________________________________________________________________________")

    print("You can then roll the die to determine your character's attribute values.\n"
          "Say you roll 6 sided die 3 times, you will get a sum of ", end="")
    print(lab05.roll_die(3, 6))

    print("__________________________________________________________________________________________________")

    print("At the end, the print character function will take list returned by create_character \n"
          "function as an argument and output..")
    character_list = lab05.create_character(syllables)
    lab05.print_character(character_list)

    print("__________________________________________________________________________________________________")

    # Bonus : append the list of purchased elements to the character list and print the entire character
    print("With item list, the print character function will output..")
    character_list.append(["Items", "Acid", "Arrows", "Battleaxe", "Blowgun", "Book", "Crossbow", "Crowbar"])
    lab05.print_character(character_list)


if __name__ == "__main__":
    main()
