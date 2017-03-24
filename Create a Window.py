import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
print('-'*((n*2)+3))
for i in range(n):
    print('|'+str(('.')*n)+'|'+str(('.')*n)+'|')
print('|'+str(('-')*n)+'+'+str(('-')*n)+'|')
for j in range(n):
    print('|'+str(('.')*n)+'|'+str(('.')*n)+'|')
print('-'*((n*2)+3))
