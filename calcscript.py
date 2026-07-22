# clean calculator script with basic validation

try:
    x = float(input("Enter your first number: "))
    y = float(input("Enter your second number: "))
except ValueError:
    print("Please enter valid numbers.")
    raise SystemExit(1)

operation = input("Choose your operation (+, -, *, /, %): ")
result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    if y == 0:
        print("Cannot divide by zero.")
    else:
        result = x / y
elif operation == '%':
    if y == 0:
        print("Cannot use modulus with zero.")
    else:
        result = x % y
else:
    print("Invalid operation. Please choose +, -, *, /, or %.")

if result is not None:
    print("Result:", result)