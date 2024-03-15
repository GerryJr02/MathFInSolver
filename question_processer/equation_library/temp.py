

# Function to create a pretty message
# Function to create a pretty message with color
def create_pretty_message():
    # Define the message
    message = "\033[1;35mHello, world! This is a pretty message.\033[0m"  # Purple color for the message

    # Add some decorations
    decorated_message = "\033[1;34m" + "*" * (len(message) + 6) + "\033[0m\n"  # Blue color for the border
    decorated_message += "\033[1;34m*\033[0m   " + message + "   \033[1;34m*\033[0m\n"  # Message with padding
    decorated_message += "\033[1;34m" + "*" * (len(message) + 6) + "\033[0m\n"

    print(decorated_message)


if "__main__" == __name__:
    create_pretty_message()
