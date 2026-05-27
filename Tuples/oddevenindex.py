def odd_even_split_tuple(tup):
    odd = ()
    even = ()
    for i in tup:
        if i % 2 == 0:
            even += (i,)
        else:
            odd += (i,)
    return odd, even

t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd, even = odd_even_split_tuple(t)
print("Odd tuple:", odd)
print("Even tuple:", even)