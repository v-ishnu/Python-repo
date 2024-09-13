# write a program to enter the numbers till the user enter ZERO and at the end it should display the count of all the numbers.

count =0

while True:
    input_number = int(input("Enter number: "))
    count +=1
    user_continue = input("Do you continue - Y/N or 0 : ").upper()
    if (user_continue == "N" or input_number == 0):
        break
print(count)