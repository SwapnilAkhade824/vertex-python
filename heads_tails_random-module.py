import random as r

print("Welcome! Let's flip a coin.\n")
a = input("Enter H for heads and T for tails: \n")
b = r.choice(['Heads','Tails'])

if a=='H'or a=='h':
	if b=='Heads':
		print("You Win!\n")
	else:
		print("You Lose....\n")

elif a=='T'or a=='t':
	if b=='Heads':
		print("You Lose....\n")
	else:
		print("You Win!\n")
		
else:
	print("Incorrect input.....")