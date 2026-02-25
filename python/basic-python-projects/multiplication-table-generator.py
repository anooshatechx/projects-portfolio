# Multiplication Table Generator

def multiplication_table(num1, num2, num3):
    while num2 <= num3:
        print(f"{num1} × {num2} = {num1*num2}")
        num2 = n2 + 1

while True:
    print("Welcome to Multiplication Table Generator!")
    try:
        num1 = int(input("Enter the number you want table of: "))
        num2 = int(input("Enter the number you want your table to start from: "))
        num3 = int(input("Enter the number you want your table to go up to: "))
    except ValueError:
        print("Please enter numbers only!")
        continue

    multiplication_table(num1, num2, num3)

    repeat = input("Do you want to generate another table? y/n: ")
    if repeat.lower() != "y":
        break

print("Thank you!!!")
