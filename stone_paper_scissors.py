'''
WAP to simulate stone, paper, scissors
'''

import random

print("Let's play Rock, Paper, Scissors!!\n")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]

c = random.choice(game)
cn = game.index(c)
print(cn)
pn = (int(input("Enter your move:\n1.ROCK\n2.PAPER\n3.SCISSORS\n: ")))-1
p = game[pn]
print('Computer:\n',c,'\n','Player:\n',p)
if pn==cn:
	print("It's a TIE!")
elif pn == 0:
	if cn == 1:
		print("You Lose....-_-")
	else:
		print("You Win!!! UwU")
elif pn == 1:
	if cn == 0:
		print('You Win!!! UwU')
	else:
		print("You Lose....-_-")
else:
	if cn == 0:
		print("You Lose....-_-")
	else:
		print('You Win!!! UwU')
