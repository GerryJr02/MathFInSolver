"""
main.py

This module is meant specifically for an upper division math class. In particular, Math 176 in UCI.
The hope is to be able to copy any question into the program and this should guide to the answer
with a couple of questions.
"""

import question_processer

def main():
    # Print Dramatic Intro
    question_processer.print_intro()

    # Get Question
    question = input("Enter your question here: ")
    print("\n"*50)

    # Map the Question with correlated equations
    correlation_map = question_processer.find_related_equations(question)

    # Pick and Run equation
    question_processer.run_equation(correlation_map)

    input("\nPress Enter to Exit...")


if __name__ == "__main__":
    main()
