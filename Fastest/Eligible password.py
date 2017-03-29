import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
l = 'false'
num = 'false'
lower = 'false'
upper = 'false'
if len(s)>=8:
    for i in s:
        if i in ('1234567890'):
            num = 'true'
        if i.islower():
            lower = 'true'
        if i.isupper():
            upper = 'true'
    l = 'true'
else:
    pass

if l == 'true' and num== 'true' and lower == 'true' and upper == 'true':
    print('true')
else:
    print('false')
            
            
