3
1 0 1

output
0

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
j = 0
n = int(input())
for i in input().split():
    x = int(i)
    j += x
if j%2==0:
    print(0)
else:
    print(1)
