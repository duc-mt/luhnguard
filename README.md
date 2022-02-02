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
prompt for a credit card number (string type)
reverse the number
FOR each digit in number
    double every second digit starting from left
    IF product > 9
        THEN sum each digit of product
    add doubled digits with the undoubled digits
IF the total modulo (%) 10 equates to 0
  THEN output 'valid'
ELSE
  THEN output 'invalid'
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

```bash
$ python3 main.py
Please enter card number: 27282902627
'27282902627' is invalid
```
