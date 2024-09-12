# Define Addition
def addition(a, b):
    return a + b

# Define Subtraction
def subtraction(a, b):
    return a - b

# Define Multiplication
def multiplication(a, b):
    return a * b

# Define Division
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Define the function
def calculator():
    print("Welcome to Command Line Calculator!")
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter operation number (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = addition(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtraction(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiplication(num1, num2)
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == '4':
                    result = division(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
            except ValueError:

                print("Error: Please enter valid numbers.")

    # After completing the operation, ask if user wants to continue
    while True:
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again == 'yes':
            calculator()
            break

        if again == 'no':
            print("Exiting calculator. Goodbye!")
            break

    # Add a prompt to keep the window open until user input
    input("\nPress Enter to exit...")

# Call the calculator function to start the program
calculator()
