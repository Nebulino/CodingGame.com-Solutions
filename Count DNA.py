import sys
import math
s = input()
rA = 0
rC = 0
rG = 0
rT = 0
for i in s:
    if i == 'A':
        rA += 1
    elif i == 'C':
        rC += 1
    elif i == 'G':
        rG += 1
    elif i == 'T':
        rT += 1
print('%s %s %s %s' % (rA, rC, rG, rT))
