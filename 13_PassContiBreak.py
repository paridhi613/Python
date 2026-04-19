#PASS 
for i in range(4):
    pass                  #this helps avoinding the syntax error



#CONTINUE
for i in range(11):
    if i == 5:
        continue          #this will skip 5 and print rest of the values
    print(i,end=" ")

print()


#BREAK
for i in range(11):
    if i == 5:
        break              #this will stop the priting here 
    print(i,end = " ")


print()


m=1
while m<=10:
    if m == 8:
        break
    print(m,end=" ")

    m += 1