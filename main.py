#!/usr/bin/python3
# -*- coding: utf-8 -*-

# =============================================================================
#
#        FILE:  main.py
#      AUTHOR:  Tan Duc Mai
#       EMAIL:  tan.duc.work@gmail.com
#        DATE:  17-Dec-2021
# DESCRIPTION:  Use Hans Peter Luhn's algorithm to validate credit card number
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#
# =============================================================================

# ------------------------------- Module Import -------------------------------
import icontract


# ---------------------------- Function Definitions ---------------------------
@icontract.require(lambda total: isinstance(total, int))
@icontract.ensure(lambda result: isinstance(result, bool))
def check_moduo_10(total):
    """
      Check if total moduo 10 is equal to 10.
      Return True if if it is; False otherwise.
    """
    # IF the total modulo 10 is equal to 0: number is valid.
    if total % 10 == 0:
       return True
    # ELSE: number is invalid.
    else:
        return False


@icontract.require(lambda number: number.isnumeric())
@icontract.ensure(lambda result: isinstance(result, int))
def add_digits(number):
    """Return the sum of doubled digits with the undoubled digits."""
    # Initialise an accumulator to 0.
    sum_digits = 0

    for index, digit in enumerate(number):
        if index % 2 == 0:
            sum_digits += int(digit)
        else:
            # Double every second digit going from left to right.
            # If greater than 10, sum the digits.
            doubled_digits = int(digit) * 2
            for each_digit in str(doubled_digits):
                # Add doubled digits with the undoubled digits.
                sum_digits += int(each_digit)

    return sum_digits


@icontract.require(lambda card_number: isinstance(card_number, str))
@icontract.ensure(lambda result: isinstance(result, str))
def reversed_number(card_number):
    """From the card number, reverse it so it goes from right to left."""
    new_number = ''

    for digit in range(len(card_number)-1, -1, -1):
        new_number += card_number[digit]

    return new_number


# ---------------------------------- Program ----------------------------------
def main():
    # Input to credit card number (as a string).
    card_number = input('Please enter card number: ')

    # Add digits up and moduo 10, display the result.
    print(f'{repr(card_number)} is', end=' ')
    if check_moduo_10(add_digits((reversed_number(card_number)))):
        print('valid')
    else:
        print('invalid')


# --------------------------- Call the Main Function --------------------------
if __name__ == '__main__':
    try:
        main()
    except icontract.errors.ViolationError as e:
        print(e)
