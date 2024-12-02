import math


def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        operation = input("Enter an operation (+, -, *, /, **, sqrt): ")
        if operation in ['+', '-', '*', '/', '**', 'sqrt']:
            break
        else:
            print("Invalid operation. Please enter a valid operation.")

    if operation == 'sqrt':
        result = math.sqrt(num1)
    else:
        while True:
            try:
                num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        elif operation == '**':
            result = num1 ** num2

    print("Result: ", result)


calculator()