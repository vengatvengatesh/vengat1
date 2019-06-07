x=int(input())
y=[]
for i in range(0,x):  
    z=input()
    y.append(z)
list=[]
for i in zip(*y):
    if i.count(i[0])==len(i): 
        list.append(i[0])
    else:
        break
print(''.join(list))
