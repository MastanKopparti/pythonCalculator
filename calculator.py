print("Welcome to the Python Calculator!")
def get_number(prompt):
    while True:
        num_str = input(prompt)
        try:
            if '.' in num_str:
                return float(num_str)
            else:
                return int(num_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operation = input("Choose an operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
