import sys
import math

l = []
m = []
n = int(input())
for i in range(n):
    line = input()
    if i%2==0:
        l.append(line)
    else:
        m.append(line)
        
for c in l:
    print(c)
for x in m:
    print(x)
