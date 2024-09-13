"""
Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False 

"""
# Prime No
# num = []
# n= int(input('Enter a number:'))


# for i in range (n):
#     no = int(input('Enter Element:'))
#     for j in range (2,n):
#         if (no % j) == 0:
#             print('Not Prime Num')
#             break
#     else:
#         print('Prime No')
#         num.append(no)
# print(num)


"""Check list element"""

#not solved

from multiprocessing.reduction import duplicate


list=[7,9,7,16,5,8,15,27]


# for i in list:
#     i = 0
#     if list[i] % i == 0:
#         print('Prime No.')
#         break
#     else:
#         print(list)


"""
Problem Statement:

You are given a list of integers. Write a Python program to perform the following tasks:

Remove Duplicates: Remove any duplicate elements from the list, maintaining the order of the first occurrence of each number.
Sort the List: Sort the remaining elements of the list in ascending order.
Sum of List: Find the sum of the list after removing duplicates and sorting.
Find Max and Min: Find the maximum and minimum values in the list.

"""
duplicacy = []
for i in list:
    if