import random as r

a = 0

while (a in [1,0]):
	a = int(input("Enter the choice 1 or 0 and any other key to exit : "))

	if(a == r.choice([1,0])):
		print("WIN")
	elif(a not in [1,0]):
		print("Thanks")
		break
	else: 
		print("LOSE")

a = [1,2,3,4,5,6,7,8,9,10]

for i in range (1,10,1):
	print(a[r.randint(0,9)])