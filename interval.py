x,y=input().split()
v=[]
d=''
for i in range(int(a)+1,int(b)):
    if i%2==1:
        v.append(i)
for i in range(len(v)-1):
    d+=str(v[i])+" "
print(d+str(v[-1]))
