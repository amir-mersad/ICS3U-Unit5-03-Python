#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: November 2019
# This program gives the percentage of levels


def percentage(level_str):
    # Process
    if level_str == "4+":
        percent_of_level = 98
    elif level_str == "4":
        percent_of_level = 90
    elif level_str == "4-":
        percent_of_level = 83
    elif level_str == "3+":
        percent_of_level = 78
    elif level_str == "3":
        percent_of_level = 75
    elif level_str == "3-":
        percent_of_level = 71
    elif level_str == "2+":
        percent_of_level = 68
    elif level_str == "2":
        percent_of_level = 65
    elif level_str == "2-":
        percent_of_level = 61
    elif level_str == "1+":
        percent_of_level = 58
    elif level_str == "1":
        percent_of_level = 55
    elif level_str == "1-":
        percent_of_level = 51
    elif level_str == "0+":
        percent_of_level = 45
    elif level_str == "0":
        percent_of_level = 35
    elif level_str == "0-":
        percent_of_level = 15
    else:
        percent_of_level = -1
    return percent_of_level


def main():
    # This function gets the input and gives the percentage

    # Input
    level = input("Please enter your level example(4+): ")

    # pass the level to function to get the percentage
    percent = percentage(level)

    # Output
    if percent == -1:
        print("Invalid input!!!")
    else:
        print("Your grade is", percent)


if __name__ == "__main__":
    main()
