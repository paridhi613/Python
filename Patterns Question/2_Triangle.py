n=int(input())
for i in range(n):              #starts from 0
    for j in range(i+1):        #i+1 values will be printed 
        print("*",end=" ")
    print()



         ##can also be written as
    # for i in range(1, n+1):
    #     for j in range(i):
    #         print("*", end = " ")
    #     print()