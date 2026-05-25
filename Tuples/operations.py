#count: gives the frequency of the elements in the tuple 

t=(1,2,3,4,5)
print(t.count(3))   #1 
print(t.count(6))   #0   gives 0 for non existing elements


#index: gives the index of the first occurrence of the element in the tuple
print(t.index(5))   #4

t1=(1,2,3,4,5,3)
print(t1.index(3))  #2   gives the index of the first occurrence of the element in the tuple


#iteration: we can iterate through the elements of the tuple using a for loop
for i in t:
    print(i**2, end=" ")   #1 4 9 16 25