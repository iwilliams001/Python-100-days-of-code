import random
print("Let's play rock paper scissors")

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

player_choice = input('What do you choose? rock, paper or scissors? You can also just type "R" or "P" or "S".\n')
player_choice = player_choice[0].lower()
rps = ["r","p","s"]
position = rps.index(player_choice)
if position == 0:
    print(f"You chose Rock{rock}")
elif position == 1:
    print(f"You chose Paper{paper}")
else:
    print(f"You chose Scissors{scissors}")

computer_choice = random.randint(0,2)

if computer_choice == 0:
    print(f"Computer chose Rock{rock}")
elif computer_choice == 1:
    print(f"Computer chose Paper{paper}")
else:
    print(f"Computer chose Scissors{scissors}")


if position != computer_choice:
    if position == 0 and computer_choice == 2:
        print("You win!")
    elif position == 1 and computer_choice == 0:
        print("You win!")
    elif position == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose!")
else:
    print("It's a tie. Play again.")
