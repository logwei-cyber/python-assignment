import random

choices = ['Stone', 'Knife', 'Paper']
YOU_WIN = "You win!"
A_TIE = "It's a tie!"
COMPUTER_WIN="Computer wins!"
choices_map={'0':'Stone','1':'Knife','2':'Paper'}
comPchoice = ['0','1','2']
computer_choice = random.choice(comPchoice)
print("The Computer's choice:", choices_map[computer_choice])
player_choice = input("Enter your choice [S, K, P]: ")
if player_choice == 'S' and computer_choice == '1':
    print(YOU_WIN)
elif player_choice == 'K' and computer_choice == '2':
    print(YOU_WIN)
elif player_choice == 'P' and computer_choice == '0':
    print(YOU_WIN)
elif player_choice == choices_map[computer_choice]:
    print(A_TIE)
else:
    print(COMPUTER_WIN)
