a = int(input('Enter any number:'))
b = int(input('Enter any number:'))
x = input('What you want:')

if x == '+':
    print("Sum = ", a+b)
elif x == '-':
    print("Sub = ", a-b)
elif x == '*':
    print("Multiply = ", a*b)
elif x == '%':
    print("Modules = " ,a%b)
elif x == '/':
    print("Remainder = ", a/b)
else:
    print("Something went wrong")