#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo 
from random import randint

guess = 0
hard_level_turns =5
easy_level_turns =10

def set_turns():
    level = input("Choose a level type 'easy' or 'hard' \n")
    if level.lower() == 'easy':
        return easy_level_turns
    elif level.lower() == 'hard':
        return hard_level_turns
    else:
      print("Incorrect level ")  
      set_turns() #recursion

def check_answer(turns,guess,answer):
    if guess > answer:
        print("Your guess is too high")
        return turns - 1
    elif guess < answer:
        print("Your guess is too low")
        return turns - 1
    else:
        print(f"You won. The quess number is {answer}")
        return
    
def play():
    print(logo)
    print("Welcome to the guessing number game")
    #print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    guess =0 #start answer will never be 0
    turns = set_turns()
    while guess != answer:
        print(f"You have {turns} attempts ")
        guess = int(input("Make a guess\n"))
        turns = check_answer(turns,guess,answer)
        if turns == 0:
            print("You have run out of attempts. You loss")
            return
        elif guess != answer:
            print('Guess again')
        
            
        
play()    
    
    
