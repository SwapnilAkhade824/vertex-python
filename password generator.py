import random as r

characters = 'abcdefghijklmnopqrstuvwxyz'
digits = '1234567890'
symbols = '`~!@#$%^&*|<>?'

password = []

char = int(input("Enter the no of Characters you want : "))
symb = int(input("Enter the no of symbols you want : "))
num = int(input("Enter the no of digits you want : "))

total_length = char + symb + num

for i in range (0,total_length-1):
	if i < char : password.append(r.choice(characters))
	elif i < (char + symb) : password.append(r.choice(symbols))
	else : password.append(r.choice(digits))

# Easier Way

password = "".join(password)

print("Your Required Password EasyOne :",password)

# Harder Way

password = list(password)

harder_password = []

index = []

for i in range (0,total_length-1):
	ch = r.choice(password)
	while password.index(ch) in index : 
		ch = r.choice(password)
	index.append(password.index(ch))
	harder_password.append(ch)

harder_password = "".join(harder_password)

print("The Harder Password can be :",harder_password)
	
