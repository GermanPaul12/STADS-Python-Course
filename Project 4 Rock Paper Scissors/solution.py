import random
your_score,computer_score = 0.0,0.0
options=["Rock", "Scissors", "Paper"]
print("Welcome to Rock Paper Scissors!")
while True:
    computer_choice = random.choice(options)
    user_choice = input("Enter 'Rock', 'Paper', 'Scissors' or 'quit': ").capitalize()
    if user_choice == "Quit":
        break
    if user_choice not in options:
        print("Please enter a valid choice!")
        continue
    if user_choice == computer_choice:
        print(f"You both have chosen {user_choice}. It'S a draw!")
        your_score += 0.5
        computer_score += 0.5
    elif (user_choice == "Rock" and computer_choice == "Paper") or (user_choice == "Scissors" and computer_choice == "Rock") or (user_choice == "Paper" and computer_choice == "Scissors"):
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You loose!")
        computer_score += 1
    else:
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
        your_score += 1
    print(f"your score: {your_score} - computer's score: {computer_score}")        
            