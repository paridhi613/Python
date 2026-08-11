#accessing data from the dictionary

fruits = {'apple': 120, 'banana': 30}
print(fruits['apple'])    #gives the value of the key 'apple'
print(fruits['banana'])   #gives the value of the key 'banana'



#using get method
print(fruits.get('apple'))    #gives the value of the key 'apple'
print(fruits.get('orange','not in my vocabulary'))  #gives a default value if the key is not found