def add():
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    print(a + b)


def substraction():
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    print(a - b)


def multiplication():
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    print(a * b)


def division():
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    print(a / b)


on = True

while on:
    operation = input("Chose the operation type +, -, *, / or q ")
    if operation == '+':
        add()
    elif operation == '-':
        substraction()
    elif operation == '*':
        multiplication()
    elif operation == '/':
        division()
    elif operation == 'q':
        on = False
    else:
        print("{} is incorrect operation".format(operation))
