# Quiz Game
dic = {"""Q1. Which planet is known as the Red Planet?
a) Earth
b) Venus
c) Mars
d) Jupiter""" : "c",
"""Q2. What is the capital of Japan?
a) Seoul
b) Beijing
c) Tokyo
d) Bangkok""" : "c",
"""Q3. Which function is used to take input from the user in Python?
a) print()
b) input()
c) str()
d) type()""" : "b",
"""Q4. What is 12 × 8?
a) 96
b) 108
c) 86
d) 88""" : "a",
"""Q5. Who wrote the theory of relativity?
a) Isaac Newton
b) Albert Einstein
c) Galileo Galilei
d) Nikola Tesla""" : "b"}
count = 0
for k,v in dic.items():
	print(k)
	user = input("Enter your answer: ")
	if user.strip().lower() == v.lower():
		print()
		print("Superb!!! You got this 🎯")
		count = count+1
	else:
		print(f"Oops! ☹️ The right answer is {v}")
	print()
print(f"Your final score is : {count}/5")
	
