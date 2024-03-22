import time


def print_intro():
    # ASCII art for "Math Finance"
    math_finance_ascii = [
        r"    __  __       _   _        _ _____ _  _   ____    ",
        r"   |  \/  | __ _| |_| |__    / |___ /| || | | __ )   ",
        r"   | |\/| |/ _` | __| '_ \   | | |_ \| || |_|  _ \   ",
        r"   | |  | | (_| | |_| | | |  | |___) |__   _| |_) |  ",
        r"   |_|  |_|\__,_|\__|_| |_|  |_|____/   |_| |____/   "
    ]
    ascii_len = max([len(line) for line in math_finance_ascii])
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
