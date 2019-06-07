a,b=[int(x) for a in input().split()]
for x in range(a,b):
  sum=0
  temp=a
  while temp > 0:
    d = temp % 10
    sum=sum + d ** 3
    temp = temp // 10
  if(a==sum):
    print(a)
