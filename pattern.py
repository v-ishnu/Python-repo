# num = 5
# for i in range (0, num):
#     a = 1
#     for j in range (0, i+1):
#         print(a, end =" ")
#         a = a+1
#     print()


num = 5
i = 1
while i <= num:
    j=1
    while j<=i:
        print(j, end= " ")
        j+=1
    print() #Print with print() can always start with new line
    i +=1