t=(1, 2, 3)
print(type(t))

t3=([3,4,5,6], "hello babee")
print(type(t3))


print(t3[0])

t3[0][0]=100
print(t3)


#only the reference of the list is stored in the tuple, not the list itself. So we can change the list but we cannot change the reference of the list in the tuple.