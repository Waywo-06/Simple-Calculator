def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation in operations:
    result = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
else:
    print("Invalid operation. Please enter +, -, *, or /.")


