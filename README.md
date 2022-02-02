# This project aims to ...
Use Hans Peter Luhn's algorithm to validate a credit card number in Python.

# Introduction
Chances are you have a credit card in your wallet or purse. Credit card numbers
have a 'checksum' built into them, a mathematical relationship between at least
one number and the others. The checksum enables a computer to detect typos, if
not fraudulent numbers, without having to query a database (which can be slow).
Most cards use an algorithm invented by Hans Peter Luhn, a scientist who worked
for IBM. According to Luhn's algorithm, this program will validate if a credit
card number is valid.

# Luhn’s Algorithm
According to Luhn’s algorithm, you can determine if a credit card number is
(syntactically) valid as follows:
```
1. Get a credit card number (as a string).
2. Double every second digit going right ot left.
3. If greater than zero:
4.   Sum the digits.
5. Add doubled digits with the ubdoubled digits.
6. If the total modulo 10 is equal to 0:
7.   The number is valid.
8. Else:
9.   The number is invalid.
```

# More Information
* [Wikipedia](http://en.wikipedia.org/wiki/Luhn_algorithm)
* [CS50](https://cs50.harvard.edu/x/2022/psets/1/credit/)

# Sample Output
```bash
$ python3 main.py
Please enter card number: 79927398713
'79927398713' is valid
```
