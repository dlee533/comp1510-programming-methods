import doctest


def im_not_sleepy() -> tuple:
    """return string with time that requires the highest number of bars and the number of bars

    :postcondition: make hours, minutes list
    :postcondition: find the most hours, minutes and the corresponding number of bars
    :return: tuple that contains string(time), int(bars)
    >>> im_not_sleepy()
    ('10:08', 21)
    """
    hours_list = [list(str(hours)) for hours in range(13)]
    minutes_list = [list("0" + str(minutes)) if minutes < 10 else list(str(minutes)) for minutes in range(60)]
    hour, num_of_segments_h = find_most_bar(hours_list)
    minute, num_of_segments_m = find_most_bar(minutes_list)
    return f"{hour}:{minute}", (num_of_segments_h + num_of_segments_m)


def find_most_bar(time_list: list) -> tuple:
    """find the most bar

    :param time_list: a list
    :precondition: time_list must be a list consists of sub lists that contains strings for each
    time it represents
    :postcondition: for each item in sublist, insert a key value pair to another dictionary,
    with key being the time and value, the number of bars it requires to form the time
    :return: tuple
    """
    segments_dict = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
    segments = {}
    for i, time in enumerate(time_list):
        segments[i] = 0
        for my_str in list(time):
            segments[i] += segments_dict[my_str]
    most_segment = max(segments.values())
    most_segment_time = list(segments.keys())[list(segments.values()).index(most_segment)]
    most_segment_time = str(most_segment_time)
    return (most_segment_time if most_segment < 9 else "0"+most_segment_time), most_segment


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
