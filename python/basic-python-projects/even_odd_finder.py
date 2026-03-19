#Even-Odd Finder
while True:
	try: 
		print("Welcome to Even-Odd Finder!")
		num = int(input("Enter a number: "))
		if num % 2 == 0:
			print(f"{num} is even")
		else:
			print(f"{num} is odd")
		repeat = input("Do you want to find another?: y/n: ")
		if repeat.lower() != "y":
			break
	except ValueError:
		print("Please enter number only!")
print("Thank you!!!")
