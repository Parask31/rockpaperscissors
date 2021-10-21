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
choice=input("What do you want to choose?Type 0 for rock 1 for paper 2 for scissors.\n")

if int(choice)==0:
  print("You choose\n",rock)
  computer_choice=random.randint(0,2)
elif int(choice)==1:
  print("You choose\n",paper)
  computer_choice=random.randint(0,2)
elif int(choice)==2:
  print("You choose\n",scissors)
  computer_choice=random.randint(0,2)
else:
  print("Wrong choice game over!!")
  exit()

if int(computer_choice)==0:
  print("computer choose\n",rock)
elif int(computer_choice)==1:
  print("computer choose\n",paper)
elif int(computer_choice)==2:
  print("computer choose\n",scissors)


if int(choice)==computer_choice:
  print("draw")
elif int(choice)==0 and computer_choice==2 or int(choice)==1 and computer_choice==0 or int(choice)==2 and computer_choice==1:
  print("You win!!")
else:
  print("You lose")

input("Press enter to exit")



