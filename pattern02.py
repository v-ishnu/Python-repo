#              1
#         1   2   1
#     1   2   3   2   1
# 1   2   3   4   3   2   1


# n = int(input("Enter the number of rows: "))
# spaces = n - 1  #Means no. of rows -1
# i = 1

# while i <= n:
#     print("  " * spaces, end="")
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     j = i - 1
#     while j >= 1:
#         print(j, end=" ")
#         j -= 1
#     print()
#     spaces -= 1
#     i += 1
    
    
#  2nd Method
n = int(input("Enter the number of rows: "))
spaces = n -1

for i in range (1, n):
    print("  " * spaces, end="")
    
    j = 1
    for j in range (j,i+1):
        print(j, end= " ")

    for j in range (j-1,0,-1):
        print(j, end=" ")
    print()
    spaces -=1
