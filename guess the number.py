import random
number = random.randint(10,50)
chance = 0
while chance <= 5:
	guess = int(input("Can you guess the correct number? Enter your number"))
	if guess == number:
		print("YOU WON! :-)")
		break
	else:
		chance +=1
if not chance <=5:
	print(f"YOU LOST! The number was {number}")