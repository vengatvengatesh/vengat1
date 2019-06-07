s1=[]
s2=[]
e=0
n1=int(input())
item=input().split()
for i in item:
  s1.append(int(i))
for i in range(0,n1-1):
  e=0
  for j in range(i+1,n1):
    if s1[i]==s1[j]:
      e=e+1
      break
  if e>=1 and s1[i] not in s2:
    s2.append(s1[i])
z=len(s2)
if z==0:
  print("unique")
else:
  for i in s2:
    print(i,end=" ")
