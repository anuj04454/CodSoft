import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "match tie!"
    elif (user_choice ==1 and computer_choice ==3) or \
         (user_choice == 3 and computer_choice ==2) or \
         (user_choice == 2 and computer_choice ==1):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nWelcome to Rock-Paper-Scissors Game!")
        print("Enter your choice:- \n*Press (1) for Rock \n *Press (2) for Paper \n *Press (3) for Scissors \n *Press (0) for exit game")
        


        user_choice = int(input("Your choice: "))

        if user_choice == 0:
            print("Thank you!")
            break
        
        if user_choice not in [1, 2, 3]:
            print("Invalid choice.")
            continue
        

        choices = [1,2,3]
        computer_choice = random.choice(choices)


        result = determine_winner(user_choice, computer_choice)

        if user_choice==1:
           a="rock"
        if user_choice==2:
           a="paper"
        if user_choice==3:
           a="scissors"

        if computer_choice==1:
           b="rock"
        if computer_choice==2:
           b="paper"
        if computer_choice==3:
           b="scissors"

        #display result
        print(f"\nYour choice: {a}")
        print(f"computer's choice : {b}")
        print(f"Result: {result}")
        
    
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        # display scores
        print(f"\nYour score: {user_score}")
        print(f"Computer's score: {computer_score}")
    
    
if __name__ == "__main__":
    main()
