d = {}
print(type(d))
print(d)


e = dict()
print(type(e))
print(e)


fruits = {'apple': 120, 'banana': 30}
print(fruits)


#using zip() function to create a dictionary
name=['jeon', 'kim', 'park']
use=['jung', 'v', 'jim']
username=dict(zip(name, use))

print(username)


print(len(username))     #gives the length of the dictionary