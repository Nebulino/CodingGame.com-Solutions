The program:
Your program must reverse the positions of each word in the sentence given as input.

INPUT:
S, a string.

OUTPUT:
A string containing all the space-separated words of S in reverse order.

CONSTRAINTS:
S contains at least one word.
S contains less than 1000 characters.

EXAMPLE:
Input
Hello World
Output
World Hello



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
s = s.split(' ')


print(' '.join(reversed(s)))
