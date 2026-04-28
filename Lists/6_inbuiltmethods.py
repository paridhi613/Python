#1. COUNT - give the count of the element present in the list
task = [133, 544, 643, 6432]
print(task.count(544))


#2. INDEX - return the index of 1st occurance of the object
print(task.index(643))


#3. POP - remove and return the last ele of the list
drop = task.pop()
print(drop)


#4. REMOVE - remove the object of our choice
task.remove(643)
print(task)


#5. SORT - sorts the list in asc by default
name =[100,345,689,908,456]
name.sort()
print(name)


#6. INSERT - inserts a new ele to the given index
name.insert(0,10)
print(name)

#7. APPEND - adds a new ele at the end of the list
name.append("paridhi")
print(name)

l1=[1,3,4]
name.append(l1)
print(name)

8. #EXTEND - adds the ele of a list to another list as a single ele
l =[1,3,4,5,6,7]
l3 = [4,5,9]
l.extend(l3)
print(l)

l4 = "apple"
l.extend(l4)
print(l)    #each letter will be added as a single ele at the end 