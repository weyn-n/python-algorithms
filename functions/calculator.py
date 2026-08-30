# addition - +
# subtraction - -
# multiplication - *
# division - /


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    elif b == 0: 
        return None
        


while True:

    first = float(input("First number: "))
    operation = input("Operation: ")
    second = float(input("Second number: "))


    if operation == "+":
        result = add(first, second)
    elif operation == "-":
        result = subtract(first, second)
    elif operation == "*":
        result = multiply(first, second)
    elif operation == "/":
        result = divide(first, second)
    else:
        print("Unknown operation")
        continue

    if result is None:
        print("Cannot divide by zero")
        continue

    if result % 1 == 0:
        result = int(result)

    print(f"Result: {result}")