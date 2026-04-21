##IN OPERATOR
name = "Paridhi Kalyane"
print("P" in name)    #true
print("w" in name)    #false


##IS OPERATOR
a=5
b=5
print(id(a), id(b))    #ids are same for both
print(a is b)          #true


c=4
print(id(a), id(c))       #ids are different of both
print(a is c)             #false