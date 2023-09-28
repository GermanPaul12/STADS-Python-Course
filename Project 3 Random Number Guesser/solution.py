import random

num = random.randrange(0,100)
while True:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess == num:
        print(f"Hurraaa you won! {guess} was the corret guess.")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y": 
            num = random.randrange(0,100)
        else:
            break    
    elif guess < num:
        print("lower")
    else:
        print("higher")
                
