fruits={"apple": 5, "banana": 3, "orange": 8}
print(fruits)

#deleting a key-value pair using pop method 
fruits.pop("banana")
print(fruits)


#deleting using popitem method
fruits.popitem()    #removes the last inserted key-value pair
print(fruits)


#deleting the whole dictionary using del method
del fruits     #deletes the whole dictionary
