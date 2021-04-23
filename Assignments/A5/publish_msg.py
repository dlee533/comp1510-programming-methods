import paho.mqtt.publish as publish


def login() -> str:
    """log the user in to the chatroom
    :postcondition: get user's nickname
    :postcondition: publish the user's nickname to let people in chatroom know the user has entered the chatroom
    :return: the nickname, string
    """
    nickname = input("What would you like your nickname to be?: ")
    publish.single("a5/admin", nickname + " has entered the chat.", hostname="test.mosquitto.org")
    return nickname


def message(nickname: str) -> None:
    """publish messages in chatroom
    :param nickname: a string
    :precondition: nickname must be a string
    :postcondition: ask user for msg
    :postcondition: if the msg is q, return
    :postcondition: publish the message
    :return: None
    """
    msg = input("(Type \"q\" to exit) >>> ")
    if msg == "q":
        publish.single("a5/admin", nickname + " has left the chat.", hostname="test.mosquitto.org")
        return
    publish.single("a5/" + nickname, msg, hostname="test.mosquitto.org")
    return message(nickname=nickname)


def main():
    """Execute the program"""
    user_name = login()
    message(nickname=user_name)


if __name__ == "__main__":
    main()
