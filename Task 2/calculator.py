 # Function to add two numbers


def add(x, y):
    return x + y


# Function to subtract two numbers1
def subtract(x, y):
    return x - y


# Function to multiply two numbers
def multiply(x, y):
    return x * y


# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


# Main function to run the calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Get user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the operation based on the user's choice
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please select a valid operation.")


# Run the calculator
calculator()
