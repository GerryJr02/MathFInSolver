import time


def print_intro():
    # ASCII art for "Math Finance"
    math_finance_ascii = [
        "  __  __       _   _            _____                                ",
        " |  \/  |     | | | |          |  ___|( )                            ",
        " | \  / | __ _| |_| |__        | |__   _ _ __   __ _ _ __   ___ ___  ",
        " | |\/| |/ _` | __| '_ \       |  __| | | '_ \ / _` | '_ \ / __/ _ \ ",
        " | |  | | (_| | |_| | | |      | |    | | | | | (_| | | | | (_|  __/ ",
        " |_|  |_|\__,_|\__|_| |_|      |_|    |_|_| |_|\__,_|_| |_|\___\___| "
    ]
    ascii_len = len(math_finance_ascii[0])
    welcome_message = "Welcome to:"
    print(f"\033[1m{welcome_message:^{ascii_len}}\033[0m")  # Note: Python 3.8 for nested f-strings

    # Print "Math Finance" line by line with a delay
    for line in math_finance_ascii:
        print(line)
        time.sleep(0.2)  # Adjust the delay as needed

    print(f"\n\033[1m{'By: Gerardo Lopez Jr.':^{ascii_len}}\033[0m")
    input("\n\nPress Enter to Continue ...")
    print("\n" * 30)

if __name__ == "__main__":
    print_intro()
