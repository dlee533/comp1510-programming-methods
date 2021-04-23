import paho.mqtt.client as client
def main():
    """
    Test the functions in this module.
    """
    def on_connect(client, userdata: None, flags: dict, rc: int) -> None:
        """
        Subscribe to a topic in MQTT.
        :param client: a module
        :param userdata: a NoneType
        :param flags: a dict
        :param rc: an int
        :precondition: client must be a module
        :precondition: userdata must be a NoneType
        :precondition: flags must be a dict
        :precondition: rc must be an int
        :postcondition: subscribes the user to a new topic to send and receive messages.
        :return: None
        """
        client.subscribe("a5/+")
    def on_message(client, userdata: None, msg) -> None:
        """
        Display message.
        :param client: a module
        :param userdata: a NoneType
        :param msg: a module
        :precondition: client must be a module
        :precondition: userdata must be a NoneType
        :precondition: msg must be a module
        :postcondition: display message.
        :return: None
        """
        print(msg.topic + " " + str(msg.payload))
    print("*~~~~~~~~~~~~~~~~~~~~*\n Welcome to the Chat!\n*~~~~~~~~~~~~~~~~~~~~*\n")
    # Create an MQTT client below
    our_client = client.Client()
    our_client.on_connect = on_connect
    our_client.on_message = on_message
    our_client.connect("test.mosquitto.org", 1883)
    our_client.loop_forever()
if __name__ == "__main__":
    main()