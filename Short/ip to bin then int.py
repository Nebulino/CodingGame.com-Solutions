s=''
i=input().split('.')
for a in i:
    s += '{0:08b}'.format(int(a))
print (int(s,2))

# or

