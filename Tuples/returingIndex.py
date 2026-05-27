def get_index(tup, elem):
    for i in tup:
        if i == elem:
            return(tup.index(elem))
    return -1


t=(10,20,30,40,50)
print(get_index(t, 30))  #2