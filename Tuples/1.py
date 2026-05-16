#tuples are created using round brackets
#they are immutable (cannot be changed after creation)

l=("hey","JK","how","are") 


#indexing
print(l[0])    #hey
print(l[-1])   #are


#slicing
print(l[1:3])   #('JK', 'how')

#are heterogeneous (can contain different data types)
t=(1,"hello",3.14,True)
print(t)
print(type(t))   #<class 'tuple'>