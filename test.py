def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", add(x, y))
    elif op == "-":
        print("Result:", subtract(x, y))
    elif op == "*":
        print("Result:", multiply(x, y))
    elif op == "/":
        try:
            print("Result:", divide(x, y))
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation.")

# test comment