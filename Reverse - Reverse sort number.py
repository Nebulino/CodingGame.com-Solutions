l=[]
ris = ''
n = int(raw_input())
for i in xrange(n):
    x = str(raw_input())
    x = str(x)
    l.append(x)
l = sorted(l, key=int, reverse=True)

print(" ".join(l))
