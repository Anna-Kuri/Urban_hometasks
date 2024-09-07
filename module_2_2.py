print('This program compares numbers!')
first = int(input('Input the first number: '))
second = int(input('Input the second number: '))
third = int(input('Input the third number: '))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
