# Math Toolkit
print("Welcome to Math Toolkit 🧮")
while True:
    print("""\nWhat do you want to do?:
a. Addition
b. Subtraction
c. Multiplication
d. Division
e. Square
f. Square Root
g. Exit
""")

    user = input("Enter your choice: ").strip().lower()

    if user in ["a", "b", "c", "d"]:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers! ✨\n")
            continue
    elif user in ["e", "f"]:
        try:
            sq = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number! ✨\n")
            continue
    elif user == "g":
        print("\nExiting Math Toolkit. Goodbye 💗")
        break
    else:
        print("Invalid choice! Please select a valid option.✨\n")
        continue

    if user == "a":
        print(f"Sum of {num1} and {num2} is: {num1 + num2}")
    elif user == "b":
        print(f"Subtract of {num1} and {num2} is: {num1 - num2}")
    elif user == "c":
        print(f"Multiplication of {num1} and {num2} is: {num1 * num2}")
    elif user == "d":
        if num2 == 0:
            print("Denominator cannot be 0. ☹️")
        else:
            print(f"Division of {num1} and {num2} is: {num1 / num2}")
    elif user == "e":
        print(f"The square of {sq} is: {sq ** 2}")
    elif user == "f":
        print(f"Square root of {sq} is: {sq ** 0.5}")

    again = input("\nDo you want another calculation? (y/n): ").strip().lower()
    if again != "y":
        print("\nGOODBYE 💌")
        break
