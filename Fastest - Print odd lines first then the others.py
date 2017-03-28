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

    
    or...
    
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
t=[]
for i in range(n):
    line = input()
    if not i%2:print(line)
    else:t+=[line]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("\n".join(t))
