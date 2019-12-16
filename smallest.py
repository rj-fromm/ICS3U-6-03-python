#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: Dec 2019
# This is program smallest number in list

import random


def smallest_number(numbers):
    # This is finds smallest number in a list

    last_number = 100

    for number in numbers:
        if number < last_number:
            smallest = number
            last_number = number

    return smallest


def main():
    # This is generate 10 random numbers

    # This is here because it wont le me use it without assignment
    smallest = 0

    # This is a list holding the random numbers
    numbers = []

    # process
    for repeater in range(0, 10):
        number = random.randint(0, 100)
        numbers.append(number)
        # output
        print(numbers[repeater])

    smallest = smallest_number(numbers)

    # output
    print("The smallest is " + str(smallest))


if __name__ == "__main__":
    main()
