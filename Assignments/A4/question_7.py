import doctest


def get_total_calories(calorie_dict: dict) -> int:
    """Calculate the sum of calories

    :param calorie_dict: a dictionary
    :precondition: calorie_dict must be a dictionary
    :postcondition: get the sum of all calories/values from calorie_dict
    :return: the sum
    >>> get_total_calories(calorie_dict={})
    0
    >>> get_total_calories(calorie_dict={'pie': 500})
    500
    >>> get_total_calories(calorie_dict={'pie': 500, 'cake': 700})
    1200
    """
    return sum(calorie_dict.values())


def print_informations(food_dict: dict) -> None:
    """Print food informations

    :param food_dict: a dictionary
    :precondition: food_dict must be a dictionary
    :postcondition: calculate total_calories
    :postcondition: calculate average_calories
    :postcondition: create a dictionary of all food item names
    :postcondition: print the information
    :return: None
    """
    total_calories = get_total_calories(food_dict)
    average_calories = total_calories/len(food_dict)
    food_items = [item for item in food_dict]
    print(f"Food Items: {food_items}\n"
          f"Total Calories: {total_calories}\n"
          f"Average Calories: {average_calories:.1f}\n")


def build_dictionary(calories=None) -> None:
    """build food dictionary

    :param calories: none or a dictionary
    :precondition: calories must be None or a dictionary
    :postcondition: prompt user to enter food item
    :postcondition: if user entered q, quit
    :postcondition: prompt user to enter calories
    :postcondition: concatenate the food info to _calories
    :postcondition: print the food information
    :postcondition: call itself with existing dictionary
    :return: None
    """
    if calories == None:
        _calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225,
                     "milk": 122, "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}
    new_item = input("Enter food item to add, or 'q' to exit: ")
    if new_item == 'q':
        return None
    new_item_calories = int(input(f'Enter calories for {new_item}: '))
    calories[new_item] = new_item_calories
    print_informations(calories)
    return build_dictionary(calories = _calories)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
