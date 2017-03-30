import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
l = ''
for i in range(n):
    l = l + " " + str(fib(i))
l = l.strip(" ")
print(l)


or

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

a = 0
b = 1
o = []
for i in range(n):
    o += [a]
    a = a+b
    b = a-b

print(*o)
