import random

def stone_knife_paper():
    options = ["Stone", "Knife", "Paper"]
    computer_choice = random.choice(options)
    user_choice = input("Enter Stone, Knife or Paper: ").capitalize()

    if user_choice not in options:
        print("Invalid choice! Please choose Stone, Knife, or Paper exactly.")
        return
    
    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == "Stone":
        if computer_choice == "Knife":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "Knife":
        if computer_choice == "Paper":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "Paper":
        if computer_choice == "Stone":
            print("You win!")
        else:
            print("Computer wins!")

stone_knife_paper()
