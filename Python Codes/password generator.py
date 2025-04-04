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
	if i < char : 
		password.append(r.choice(characters))
	elif i < (char + symb) : 
		password.append(r.choice(symbols))
	else : 
		password.append(r.choice(digits))

# Easier Way

password = "".join(password)

print("Your Required Password EasyOne :",password)

# Harder Way

harder_password = []

index = []

for i in range (0,len(password)):
	place = r.randint(0,len(password)-1)
	while place in index : 
		place = r.randint(0,len(password)-1)
	index.append(place)
	harder_password.append(password[place])

harder_password = "".join(harder_password)

print("The Harder Password can be :",harder_password)
	
