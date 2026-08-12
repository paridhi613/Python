#updating existing values
fruits={'apple': 34, 'banana':59}
fruits['apple'] = {'small':20, 'big':49}
print(fruits)


#updating a new value 
fruits['guava']=48
print(fruits)    #guava will be added to the dict


#updating a whole new dictionary in the existing dictionary
new={'kiwi': 20, 'mango': 30}
fruits.update(new)
print(fruits)    #new dictionary will be added to the existing dictionary


#citizenship check
print('kiwi' in fruits)    #gives True if the key is present in the dictionary