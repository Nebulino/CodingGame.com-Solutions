# @-|4|-@
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
tot = 0
n = int(input())
for i in range(n):
    test = input()
    for j in test:
        if j == '|':
            tot += 1
print(int(tot/2))
