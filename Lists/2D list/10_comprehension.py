l=[]
 
for i in range(10):
   l.append(i)
print(l)



#more easier way 
l=[i for i in range(14)]
print(l)


#to print the square of each element in l
l=[i**2 for i in range(10)]
print(l)


#print even numbers from 0 to 10
l=[i for i in range(10) if i%2==0]
print(l)