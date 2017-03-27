Transform an int into binary and count how many 1 on it!

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    x = int(input())
    print(bin(x).count("1"))
