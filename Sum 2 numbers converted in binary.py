You must add the binary representation of each pair of numbers and output them.

NOTE: When converting each integer to binary, (before adding each binary value as an integer,) the least significant bit is the rightmost bit.

Example:
13 -> 1101
Input
Line 1: An integer N for the count of number pairs to follow.
Next N lines: Two space separated integers i and j for the numbers to be converted to binary and added together as integer values.

def m(x): return int(bin(int(x))[2:])
for i in range(int(input())):print(sum(map(m,input().split())))
