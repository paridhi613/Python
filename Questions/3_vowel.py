text = input("enter the word: ")

for ch in text:
    if ch.lower() in "aeiou":      
        print(ch, end=" ")


#this will print all the vowels found in the sent