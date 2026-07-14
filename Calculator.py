# Simple Calculator

def calculator():
    print("\n===== SIMPLE CALCULATOR =====")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose an Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = num1 + num2
        print(f"\nResult = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"\nResult = {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"\nResult = {result}")

    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult = {result}")
        else:
            print("\nError: Division by zero is not allowed.")

    else:
        print("\nInvalid choice!")


calculator()