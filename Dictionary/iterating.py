#for loop in dictionary
fruits={'apple': 34, 'banana':59, 'guava':48}
for i in fruits:
    print(i)  #prints the keys of the dictionary

print("")  #prints a new line

for i in fruits:
    print(fruits[i])  #prints the values of the dictionary


print("")  #prints a new line

for i in fruits:
    print(i, fruits[i])  #prints the key-value pair of the dictionary



print()

#using dict.items() method
for key, value in fruits.items():
    print(key, value)    #prints the key-value pair of the dictionary using items() method