x = int(input())
a = input().split()
b = []
for i in range(0,x):
  b.append(int(a[i]))
print(min(b))
