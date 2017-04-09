s=''
i=input().split('.')
for a in i:
    s += '{0:08b}'.format(int(a))
print (int(s,2))

# or

print("".join([bin(int(i))[:2].zfill(8) for i in input().split(".")])
      
