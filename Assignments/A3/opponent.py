import random


def create_instructor():
    """Create an instructor

    :postcondition: create an instructor character with random name and assignments
    :return: the instructor dictionary
    """
    names = ["chris", 'shravan', 'sam', 'takashi', 'neda', 'amir']
    assignments = ['presentation', 'group project', 'lab', 'docstring', 'doctest', 'quiz', 'unittest',
                   'midterm', 'final']
    assignment = random.choice(assignments)
    instructor_info = {'name': random.choice(names), 'type': 'instructor', 'stress': 50,
                       'assignment': assignment}
    return instructor_info
