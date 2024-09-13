"""
You are given a list of integers. Write a Python program to perform the following tasks:

Split into Even and Odd Lists: Separate the list into two new lists — one containing all the even numbers and the other containing all the odd numbers.
Sort Both Lists: Sort both the even and odd lists in descending order.
Merge the Lists: Merge the sorted even and odd lists back together, where all the even numbers appear before the odd numbers.
Calculate Product: Calculate the product of all numbers in the final merged list.
Example:

Input: [3, 6, 2, 7, 8, 5]

Output:

c
Product: 10080

"""

numbers = [8, 7, 57, 73, 68, 83, 56, 70]

# Even List
Even_number = []
for i in numbers:
    if i%2 == 0:
        Even_number.append(i)
print("Even Numbers: ", Even_number)

# Odd Number
Odd_number = []
for i in numbers:
    if i%2 != 0:
        Odd_number.append(i)
print("Odd Numbers: ",Odd_number)

# Merge List
print ("Merge List: ", Even_number + Odd_number)

# Product
Product = 1
for i in numbers:
    Product *= i
print("Product: ", Product)

