s=input()
n=0
for i in s:
 if n<0:break
 if i=="(":n+=1
 else:n-=1
if n==0:print("true")
else:print("false")
