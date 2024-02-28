import random

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
game_choice=[rock,paper,scissors]
user_choice=int(input("Type 0 for Rock , 1 for Paper , 2 for Scissors:\n"))
if(user_choice>3):
  print("Invalid Choice ! Computer Wins!")
computer_choice=random.randint(0,2)
if computer_choice==0 and user_choice==2:
   print("Computer Choice:  \n")
   print(game_choice[computer_choice])
   print("You choose :\n")
   print(game_choice[user_choice], "\n")
   print("You lose")
elif computer_choice==1 and user_choice==0:
   print("Computer Choice:  \n")
   print(game_choice[computer_choice])
   print("You choose :\n")
   print(game_choice[user_choice], "\n")
   print("You lose!!")
elif computer_choice==user_choice:
   print("Computer Choice:  \n")
   print(game_choice[computer_choice])
   print("You choose :\n")
   print(game_choice[user_choice], "\n")
   print("Draw")
elif computer_choice==2 and user_choice==0:
   print("Computer Choice:  \n")
   print(game_choice[computer_choice])
   print("You choose :\n")
   print(game_choice[user_choice], "\n")
   print("You win!!")
  
elif computer_choice==0 and user_choice==1:
   print("Computer Choice:  \n")
   print(game_choice[computer_choice])
   print("You choose :\n")
   print(game_choice[user_choice], "\n")
   print("You win!")
elif computer_choice==1 and user_choice==2:
   print("Computer Choice:  \n")
   print(game_choice[computer_choice])
   print("You choose :\n")
   print(game_choice[user_choice], "\n")
   print("You win!!")
elif computer_choice==0 and user_choice==1:
 print("Computer Choice:  \n")
 print(game_choice[computer_choice])
 print("You choose :\n")
 print(game_choice[user_choice], "\n")
 print("You lose")

