#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg
from math import factorial

# decoration
print(stylize("\n---- | Get n-th row of pascals triangle | ----\n", fg("red")))

# user interaction
pascals_row = int(input("Enter row number: "))

# function
def triangle(n):
    row = ""
    if n == 0:
        return 0
    for k in range(n+1):
        row += str(int(factorial(n)/(factorial(k)*(factorial(n-k))))) + " "
    return row

output = stylize(triangle(pascals_row), fg("red"))
print(f"\nPascals row number {pascals_row}:\n{output}\n")
