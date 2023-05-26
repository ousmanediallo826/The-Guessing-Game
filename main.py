# Choosing a random number between 1 to 100.

from random import randint



EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """ Check answer against guess. Returns the number of number of turns remaining"""
  if guess > answer:
    print("Too High.")
    
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  elif guess == answer:
    print(f"You got it! The answer was {answer}.")

# Make a function to set the difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard':")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  
  
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 to 100.")
  answer = randint(1,100)
  
  
  turns = set_difficulty()
  
  # Let a User guess a number
  guess = 0
  #Repeat the guessing functionality if they get it wrong.
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    turns = check_answer(guess, answer, turns)
   
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again")

game()
    
    # Track the number of turns and reduce by 1 if they it wrong.
  
  
  #Repeat the guessing functionality if they get it wrong
  
  
