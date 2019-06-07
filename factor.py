num1 = int(input())
fact = 1
if num1 == 0:
   print("1")
else:
   for x in range(1,num1 + 1):
       fact = fact*x
   print(fact)
