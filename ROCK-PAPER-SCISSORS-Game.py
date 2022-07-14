# Day 4 project
import random
print("Welcome to ROCK-PAPER-SCISSORS Game!")
user_choose=int(input("What do you choose? Type 0 for Rock ,1 for Paper or 2 for Scissors.\nEnter the your choose = "))
if user_choose>=3 or user_choose<0:
    print("You Enter Invalid Choose.\nYou lose.") 
else:
    print("Your Choose is:")
# Rock
    if user_choose == 0:
        print("""
            ________
        ---'     ___)_
                (_____)
                (_____)
                (____)
        ---.____(___)
        """)
# Paper
    elif user_choose == 1:
        print("""
            ________
        ---'    ____)_____
                    ______)_
                     _______)
                   _______)
        ---.__________)
        """)
# Scissors
    else :
        print("""
            _______
        ---'    ___)______
                    ______)_
                 ___________)
                (____)
        ---.____(___)
        """)
    
    print("Computer Choose is:")
    computer_choose=random.randint(0,2)

    if computer_choose == 0:
        print("""
            ________
        ---'     ___)_
                (_____)
                (_____)
                (____)
        ---.____(___)
        """)

    # Paper
    elif computer_choose == 1:
        print("""
            ________
        ---'    ____)_____
                    ______)_
                     _______)
                   _______)
        ---.__________)
        """)

    # Scissors
    else:
        print("""
            _______
        ---'    ___)______
                    ______)_
                 ___________)
                (____)
        ---.____(___)
        """)
        
    #Handling Wins.
    if user_choose ==0 and computer_choose==2:
        print("Congratulation.You Win!.")    
    elif user_choose ==1 and computer_choose==0:
        print("Congratulation.You Win!.")    
    elif user_choose ==2 and computer_choose==1:
        print("Congratulation.You Win!.")
    #Handling Draw.      
    elif user_choose ==0 and computer_choose==0:
        print("Game Draw.")  
    elif user_choose ==1 and computer_choose==1:
        print("Game Draw.")  
    elif user_choose ==2 and computer_choose==2:
        print("Game Draw.") 
    #Handling lose.      
    else:
        print("Sorry.You Lose.")      