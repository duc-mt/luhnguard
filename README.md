# What the project does ?
Use Hans Peter Luhn's algorithm to validate a credit card number in Python.

# General Description
Chances are you have a credit card in your wallet or purse. Credit card numbers
have a 'checksum' built into them, a mathematical relationship between at least
one number and the others. The checksum enables a computer to detect typos, if
not fraudulent numbers, without having to query a database (which can be slow).
Most cards use an algorithm invented by Hans Peter Luhn, a scientist who worked
for IBM. According to Luhn's algorithm, this program will validate if a credit
card number is valid.

# Detailed Description (adopted from
[CS50](https://cs50.harvard.edu/x/2022/psets/1/credit/))
A credit (or debit) card, of course, is a plastic card with which you can pay
for goods and services. Printed on that card is a number that is also stored in
a database somewhere, so that when your card is used to buy something, the
creditor knows whom to bill. There are a lot of people with credit cards in this
world, so those numbers are pretty long: American Express uses 15-digit numbers,
MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. And
those are decimal numbers (0 through 9), not binary, which means, for instance,
that American Express could print as many as 10^15 = 1,000,000,000,000,000
unique cards! (That is, um, a quadrillion.)

Actually, that is a bit of an exaggeration, because credit card numbers actually
have some structure to them. All American Express numbers start with 34 or 37;
most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some
other potential starting numbers which we will not concern ourselves with for
this problem); and all Visa numbers start with 4. But credit card numbers also
have a “checksum” built into them, a mathematical relationship between at least
one number and others. That checksum enables computers (or humans who like
Maths) to detect typos (e.g., transpositions), if not fraudulent numbers,
without having to query a database, which can be slow. Of course, a dishonest
mathematician could certainly craft a fake number that nonetheless respects the
mathematical constraint, so a database lookup is still necessary for more
rigorous checks.

# More Information
[Wikipedia](http://en.wikipedia.org/wiki/Luhn_algorithm)
