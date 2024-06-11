def calculator():
    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display operation choices
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user to choose an operation
    choice = input("Enter the operation (1/2/3/4): ")

    # Perform the calculation based on the user's choice
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = '/'
        else:
            return "Error! Division by zero."
    else:
        return "Invalid input."

    # Display the result
    return f"The result of {num1} {operation} {num2} is: {result}"

# Run the calculator function
print(calculator())
