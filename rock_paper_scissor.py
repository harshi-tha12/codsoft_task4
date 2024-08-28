import random
def getuser_choice():
    while True:
        user_input=input("Choose 'R' for rock,'P' for paper and 'S' for scissor:").strip().lower()
        if user_input in ['r','p','s']:
            return user_input
        else:
            print("Invalid choice!!\nPlease Choose 'R' for Rock, 'P' for Paper, 'S' for Scissor:")
        
def getcomputer_choice():
    return random.choice(['r','p','s'])
def winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "TIE"
    elif(user_choice=='r' and computer_choice=='s') or (user_choice=='p' and computer_choice=='r') or (user_choice=='s' and computer_choice=='p'):
        return "user"
    else:
        return "computer"
def display_result(user_choice,computer_choice,result):
    choice={'r':'Rock','p':'Paper','s':'Scissor'}
    print(f"You chose: {choice[user_choice]}")
    print(f"Computer chose: {choice[computer_choice]}")
    if result=="TIE":
        print("**IT IS A TIE**")
    elif result=="user": 
        print("!!!YOU WINN!!!")
    else:
        print("...YOU LOSE...")
def game():
    user_score=0
    computer_score=0
    print("\n!*WELCOME TO ROCK-PAPER-SCISSOR GAME*!")
    while True:
        user_choice=getuser_choice()
        computer_choice=getcomputer_choice()
        result=winner(user_choice,computer_choice)
        display_result(user_choice,computer_choice,result)
        if result=="user":
            user_score +=1
        elif result=="computer":
            computer_score +=1
        print(f"Current score:- Your score: {user_score} | Computer score: {computer_score}")
        play_again=input("Do you want to play another round? (yes/no):").strip().lower()
        if play_again!='yes':
            print("Final score!..")
            print(f"Your score: {user_score} | Computer score: {computer_score}")
            print("THANK YOU FOR PLAYING!!!!")
            break
game()
            






