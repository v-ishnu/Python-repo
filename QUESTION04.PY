"""
Problem Statement:

You are given a list of integers. Write a Python program to perform the following tasks:

Remove Duplicates: Remove any duplicate elements from the list, maintaining the order of the first occurrence of each number.
Sort the List: Sort the remaining elements of the list in ascending order.
Sum of List: Find the sum of the list after removing duplicates and sorting.
Find Max and Min: Find the maximum and minimum values in the list.

"""

numbers = [56, 7, 57, 7, 8, 83, 56, 70]

# Remove Duplicacy

Remove_duplicacy = []
for i in numbers:
    if i in Remove_duplicacy == numbers:        
print("Duplicacy Removed Number : ", Remove_duplicacy)
