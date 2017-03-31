import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

c = input()

try:
    s = c.index('write') + len('write') +1
    e = c.index('.')
    t = 1
        
    
    if 'times' in c:
        t = c.index('times') -2
        
        n = ''
        while c[t] in '0123456789':
            n += c[t]
            t -= 1
        t = int(n[::-1])
        
    for i in range(t):
        print(c[s:e])

except:
    print('Syntax Error')
