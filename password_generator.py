import random

print("Welcome to Password Generator! Enter your requests for generating a password:")
u_alph = int(input("Enter number of uppercase letters: "))
l_alph = int(input("Enter number of lowercase letter: "))
num = int(input("Enter number of digits: "))
sp = int(input("Enter number of special characters: "))

u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = 'abcdefghijklmnopqrstuvwxyz'
n = '1234567890'
s = '!@#$%^&*-_'

p = []

for i in range(u_alph):
	p.append(random.choice(u))
for i in range(l_alph):
	p.append(random.choice(l))
for i in range(num):
	p.append(random.choice(n))
for i in range(sp):
	p.append(random.choice(s))

random.shuffle(p)
pas = ''.join(p)
print(pas,'is your newly generated password!')