#to check whether the string is pallindreome or not 

s = input()

if s== s[::-1]:   #this reverses the string 
    print("yes it is a palindrome")
else:
    print("not its not ")