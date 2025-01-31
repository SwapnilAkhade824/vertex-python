# # Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
# Example Interaction
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.

bill = 0

print("-"*100)
print(f"\n{"\t"*4}Welcome to our Pizza Service\n")
print("-"*100,"\n")

while True:
	ch = input("Enter your choice for size of the Pizza (S,M,L) : ").lower()

	if ch == 's' : 
		bill += 15

		ch = input("Add pepperoni for pizza (Y or N) : ").lower()

		if ch in 'yn':		
			if ch == 'y' :
				bill += 2
		else : 
			print("Invalid Choice!!!")
			break

	elif ch == 'm' : 
		bill += 20

		ch = input("Add pepperoni for pizza (Y or N) : ").lower()

		if ch in 'yn':		
			if ch == 'y' :
				bill += 3
		else : 
			print("Invalid Choice!!!")
			break

	elif ch == 'l' :
		bill += 25

		ch = input("Add pepperoni for pizza (Y or N) : ").lower()

		if ch in 'yn':		
			if ch == 'y' :
				bill += 3
		else : 
			print("Invalid Choice!!!")
			break
	else : 
		print("Invalid Choice!!!")
		break

	ch = input("Add extra cheese for the pizza (Y or N) : ").lower()

	if ch in 'yn':		
		if ch == 'y' :
			bill += 1
	else : 
		print("Invalid Choice!!!")
		break

	print("Your Final Bill is : $",bill)
	print("Thanks for using our service hope you enjoyed !")
	break


