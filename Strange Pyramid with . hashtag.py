

n=int(input())
l=[]
for i in range(n):
    l+=[input()]
r=int(input())
s=[int(i) for i in input().split()]
for i in range(n):
    j=(l[i]+"".join('#'if int(s[y])>=n-i else "." for y in range(r)))
    print(j)
