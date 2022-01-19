#A Simple calculator, to help you get started with python

value1= input("Enter first value:")
value2= input("Enter second value:")
v1=int(value1)
v2=int(value2)

choice =input("Enter 1 for addition.\nEnter 2 for subtraction.\nEnter 3 for multiplication.\nEnter 4 for division.\nEnter 5 for evaluation.\n:")
choice=int(choice)

if choice == 1:
    print(f'You entered {v1} and {v2} and their addition is {v1 + v2}')
elif choice == 2:
    print(f'You entered {v1} and {v2} and their subtraction is {v1 - v2}')
elif choice == 3:
    print(f'You entered {v1} and {v2} and their multiplication is {v1 * v2}')
elif choice == 4:
    print(f'You entered {v1} and {v2} and their division is {v1 / v2}')
elif choice == 5:
    print(f'You entered {v1} and {v2} and their evaluation is {v1 ** v2}')
else:
    print('you have entered wrong data , try again')
