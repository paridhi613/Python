##OUTPUT
# n= 4
#       *
#      ***
#     *****
#    *******
#   *********



n= int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
          print(" ", end = " ")
        else:
           print("*",end=" ")
    
    for j in range(i-1):
            print("*",end=" ")
    print()