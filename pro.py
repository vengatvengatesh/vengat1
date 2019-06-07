from itertools import combinations
b,v=map(int,input().split())
s=len(str(b))
a=list(combinations(str(b),s-v))
a=(sorted(a))
b="".join(a[0])
print(b)
