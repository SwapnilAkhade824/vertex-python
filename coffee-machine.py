# Main Menu (Coffee Selection)

# Espresso – $2.50
# Cappuccino – $3.50
# Latte – $4.00
# Americano – $3.00
# Mocha – $4.50
# Macchiato – $3.75
# Hot Water – $0.50
# Exit

# Size Selection (Additional Cost)

# Small – No extra charge
# Medium – +$0.50
# Large – +$1.00

# Extra Add-ons (Each item adds to the total price)

# Sugar – Free
# Milk – +$0.25
# Extra Shot of Espresso – +$1.00
# Whipped Cream – +$0.50
# Caramel Syrup – +$0.75
# Vanilla Syrup – +$0.75
# No Add-ons – No extra charge

main_menu = ["Espresso","Cappuccino","Latte","Americano","Mocha","Macchiato","Hot Water","Exit"]

base_price = [2.5, 3.5, 4.3, 4.5, 3.75, 0.5]

size_menu = ["Small","Medium","Large"]

size_price = [0, 0.5, 1]

extra_addons_menu = ["Sugar","Milk","Extra Shot of Espresso","Whipped Cream","Vanilla Syrup","No Add-ons"]

addons_price = [0, 0.25, 1, 0.5]

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

	amount = base_price[choice_size-1] + size_price[choice_size-1] + addons_price[choice_addons-1]

	print("\nYour Coffee is Ready: \n")

	print(f"\t{size_menu[choice_size-1]} : {main_menu[choice_coffee-1]} With Added {extra_addons_menu[choice_addons-1]}.\n")

	print(f"\t\tYour Total for The Order : ${amount:.2f}/-\n")