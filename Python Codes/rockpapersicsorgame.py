import random as r
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

ch = input("Enter your choice R (rock) P (paper) S (scissors) : ").upper()

if (ch in ['R','P','S']):
    if(ch == 'R'): ch = 0
    elif(ch == 'P'): ch = 1
    else: ch = 2
    print(f"Your Choice :  {game[ch]}")
    engch = r.randint(0,len(game)-1)
    print(f"Engines Choice : {game[engch]}")
    print("\nResult\n")
    if(ch==engch): print("Tie")
    elif(ch == 0 and engch == 2 or ch == 1 and engch == 0 or ch == 2 and engch == 1): print("\tWin\n")
    else: print("\tLost\n")
else: print("Invalid Choice!!!")
