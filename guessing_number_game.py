""" 
Guessing Number Game in python

Author: Tomasz Furmanczyk

"""


import random
import sys

# The intro to the game
print("Welcome to the one and only Number Guessing Game")

#Asking for the player name
name = input("What is your name: ")	
print(f"We are ready to begin {name}!")




# method for the start of the game begin_game()
def main():
	
  # declare all variables for use
  opps = 1
  # computer generated random number between 1 and 10
  ran_num = random.randint(1,10)
  #user default is zero before enter in the while loop
  user = 0
  
  
  
  
  #Loop for the user to guess the random number correctly
  while user != ran_num:
  
    try:
        user = int(input("Select a number between 1 and 10: "))
        if user < 1 or user > 10:
          print(f"You selected a number {user} that was outside of the parameters. Please try again and select a number between 1 and 10....")
          continue
    
    except ValueError:
        print(f"You selected a number {user} that was outside of the parameters. Please try again and select a number between 1 and 10....")
        
    else:
        if user > ran_num:
          opps += 1
          print("Getting closer but still too high...Please try again: ")
          
        elif user < ran_num:
          opps += 1
          print("Getting closer but still too low...Please try again: ")
  else:
    
    print(f"You have selected the correct {ran_num} within {opps} opportunities")
    return opps



# Returns the score/opps of the game that was just played
score = main()

#declare that the user selects yes or no to continue playing guessing game Y/N

user_play_again = "Y"
while user_play_again == "Y":
  new_score = 0
  user_play_again = input("Would you like to continue playing the guessing game again: Y/N  ").upper()
  
  if user_play_again == "Y":
    
    print(f"thanks for playing your score was {score}")
    score = main()
    
    if new_score > score:
      score = new_score
    else:
      score
  else:
      print(f"Good luck! Come back again {name}")
      sys.exit()
      

if __name__ == "__main__":
  main()