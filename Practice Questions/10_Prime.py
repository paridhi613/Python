#to check whether the given integer is prime or not 

n= int(input())
is_Prime = True

for i in range(2,n):
    if n%i==0:
       is_Prime= False
       break

if is_Prime:
  print("prime")
else:
   print("not prime")



