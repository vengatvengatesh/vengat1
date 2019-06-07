n,a,d=input().split()
d=1
e=0
while(d<=int(n)):
   e=e+int(a)
   a=int(a)+int(d)
   d=d+1
print(e)
