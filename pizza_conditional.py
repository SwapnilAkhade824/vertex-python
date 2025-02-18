'''WAP Based on a user's order, work out their final bill. Use the input() function 
to get a user's preferences and then add up the total for their order 
and tell them how much they have to pay.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Interaction
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $28."
'''

s = (input("Welcome! Here are the different sizes of Pizza:\nSmall pizza (S): $15\nMedium pizza (M): $20\nLarge pizza (L): $25\nChoose a size(S/M/L): "))
price = 0


if s=='S' or s=='s':
	price+=15
	print("\nChoose Toppings:\n")
	p = input("Add pepperoni (Y or N): +$2 ")
	c = input("\nAdd extra cheese (Y or N): +$1 ")
	if p == 'Y' or p == 'y':
		price+=2
	if c=='Y'or c=='y':
		price+=1
elif (s=='M' or s=='m'):
	price+=20
	print("\nChoose Toppings:\n")
	p = input("Add pepperoni (Y or N) +$3: ")
	c = input("\nAdd extra cheese (Y or N) +$1: ")
	if p == 'Y' or p == 'y':
		price+=3
	if c=='Y'or c=='y':
		price+=1
elif (s=='L' or s=='l'):
	price+=25
	print("\nChoose Toppings:\n")
	p = input("Add pepperoni (Y or N) +$3: ")
	c = input("\nAdd extra cheese (Y or N) +$1: ")
	if p == 'Y' or p == 'y':
		price+=3
	if c=='Y'or c=='y':
		price+=1

print("\nYour final bill is: ",price)