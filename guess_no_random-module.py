import random as r

a = int(input("Enter 0 or 1 : "))

b = r.randint(0,1)

if a==b:
	print("Success")
else:
	print("Fail")