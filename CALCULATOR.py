def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

print("Welcome to Simple Calculator")

while True:
    print("\nOperations:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("Q : Quit")

    choice = input("Enter operation (+ / - * / Q to quit): ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print("Result:", add(num1, num2))
        elif choice == '-':
            print("Result:", subtract(num1, num2))
        elif choice == '*':
            print("Result:", multiply(num1, num2))
        elif choice == '/':
            print("Result:", divide(num1, num2))
    elif choice.upper() == 'Q':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
