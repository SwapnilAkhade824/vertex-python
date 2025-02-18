# Main Menu:
# Espresso
# Cappuccino
# Latte
# Americano
# Mocha
# Macchiato
# Hot Water
# Exit

# Size Selection:
# Small
# Medium
# Large

# Extra Add-ons:
# Sugar
# Milk
# Extra Shot of Espresso
# Whipped Cream
# Caramel Syrup
# Vanilla Syrup
# No Add-ons

main_menu = ["Espresso","Cappuccino","Latte","Americano","Mocha","Macchiato","Hot Water","Exit"]

size_menu = ["Small","Medium","Large"]

extra_addons_menu = ["Sugar","Milk","Extra Shot of Espresso","Whipped Cream","Vanilla Syrup","No Add-ons"]

while True:
	
	print("-"*25," Welcome To the Coffee Machine ","-"*25)

	print("\nMenu:\n")

	for i in range(len(main_menu)):

		print(f"{i+1}.{main_menu[i]}.")

	choice_coffee = int(input("\nEnter your Choice: "))

	# checking for the invalid choice

	if choice_coffee not in range(len(main_menu)):

		print("Invalid Choice !!!")

		continue

	if choice_coffee == len(main_menu): break

	print("\nSelect The Size:\n")

	for i in range(len(size_menu)):

		print(f"{i+1}.{size_menu[i]}.")

	choice_size = int(input("\nEnter your Choice: "))

	# checking for the invalid choice

	if choice_coffee not in range(len(size_menu)):

		print("Invalid Choice !!!")

		continue

	print("\nSelect Extra Add-ons:\n")

	for i in range(len(extra_addons_menu)):

		print(f"{i+1}.{extra_addons_menu[i]}.")

	choice_addons = int(input("\nEnter your Choice: "))

	# checking for the invalid choice

	if choice_coffee not in range(len(extra_addons_menu)):

		print("Invalid Choice !!!")

		continue

	print("\nYour Coffee is Ready: \n")

	print(f"\t{size_menu[choice_size-1]} : {main_menu[choice_coffee-1]} With Added {extra_addons_menu[choice_addons-1]}.\n")