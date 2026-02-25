# Calculator
def calculator(num1, num2, operation):
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "×":
            return num1 * num2
        elif operation == "÷":
            return num1 / num2
        elif operation == "^":
            return num1 ** num2
        elif operation == "%":
            return num1 % num2
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "Denominator cannot be 0"

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose an operation (+,-,×,÷,^,%): ")
        result = calculator(num1, num2, operation)
        print(f"{num1} {operation} {num2} = {result}")
        
        repeat = input("Do you want another calculation? (y/n): ").strip().lower()
        if repeat != "y":
            break
    except ValueError:
        print("Please enter a valid number!")

print("Thank you!!!")
