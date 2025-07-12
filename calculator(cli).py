def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def get_op():
    while True:
        op = input("Choose operation (+, -, *, /): ").strip()
        if op in ['+', '-', '*', '/', 'x', 'X', '÷']:
            return op
        print("Invalid operation. Please choose one of +, -, *, /.")
def calc(n1, n2, operation):
    if operation == '+':
        return add(n1, n2)
    elif operation == '-':
        return sub(n1, n2)
    elif operation in ['*', 'x', 'X']:
        return mul(n1, n2)
    elif operation in ['/', '÷']:
        return div(n1, n2)

def calculator():
    print("--- Simple Calculator ---")
    while True:
        try:
            n1 = float(input("Enter the first number: "))
            operation = get_op()
            n2 = float(input("Enter the second number: "))
            result = calc(n1, n2, operation)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {n1} {operation} {n2} = {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Thank you for using the calculator!")
            break
calculator()
