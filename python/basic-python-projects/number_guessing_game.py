#Number Guessing Game
print("Welcome to Number Guessing Game!!! 🤯")
import random
print("I picked a number between 1 and 20. You have 5 attempts!")
while True:
	guess = random.randint(1,20)
	for attempt in range(1,6):
		try:
			num = int(input(f'Attempt {attempt} - Guess a number: '))
			if num > guess:
				print("Ohh no!!! Too High 📈")
			elif num < guess:
				print("Too Low! 📉")
			elif num == guess:
				print("Yayyy!!! You got it correct 🎯🔥")
				print(f"The correct number is: {guess}")
				print(f"Your attempts: {attempt}")
				print("Thanks for playing!💗")
				break
		except ValueError:
			print("Please enter a number only!")
	else:
		print(f"Out of attempts ☹️. The number was {guess}")
	repeat = input("Do you want to play again? y/n: ")
	if repeat.lower() != "y":
		print("Thanks for playing!💗")
		break
