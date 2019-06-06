x=int(input())
n=x
c=0
while(n!=0):
    b = n%10
    c = c*10 + b
    n=n//10
if c==x:
    print('yes')
else:
    print('no')
