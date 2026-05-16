#creates an empty tuple 
t=()
t1=tuple()

print(t)
print(t1)





#for creating a non empty tuple
t3=(3,)               #we need to add a comma to make it a tuple, otherwise it will be considered as an integer
print(t3)
print(type(t3))       #<class 'tuple'>




#we can also create a tuple using the tuple() constructor
t3=tuple("jungkook")
print(t3)            #('j', 'u', 'n', 'g', 'k', 'o', 'o', 'k')
#the string is converted into a tuple of characters