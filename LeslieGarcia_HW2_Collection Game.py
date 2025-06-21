print("\033[2J\033[H", end="", flush=True) # clears, ensures no new line
# and ensures immediate print
# the ansi code here is interpreted as clearing the screen with `\033[2J` but it
# doesn't move the cursor back to the beginning which is why `\033[H` is used x=5\


@author: lesliedoloresgarcia

@Course: INF 6050
@University: Wayne State University
@Assignment: Homework #2 - Collection Game
    
@Python Version: 3.11

@Required Modules: 
import sys  # For exiting the program gracefully with sys.exit()
import time       # (Optional) To add delays for better user experience
import random     # (Optional) For hint feature (randomly show a remaining item)

@Description: Build a program using: Dictionaries for metadata, Lists to hold collections,User-defined functions, Loops and logic control, and Type checking

# Clears ensures no new line and ensures immediate print
## Sequence of commands to the terminal which clears the screen and moves the cursor to the top-left
### Effectively providing a clean slate. 
print("\033[2J\033[H", end="", flush=True) 


#Importing modules
import sys  
import time
import random

# 1) Display welcome message./Option to quit anytime.

def display_welcome():
    print("Welcome to the Collection Game! ")
    print("In this game each player will enter their demographic information ")
    print("Along with a collection of three unique items. ")
    print ("Then you'll take turns guessing items in each other's items. ")
    print ("Take turns guessing the other players' items")
    print("Type 'Q' at any time to Quit the game.\n")   #Option to quit anytime.


# 2) Collect player demographic information:
## Have each player provide at least three pieces of demographic data./ Store in a dictionary.

def collect_player_info(player_num):
    print(f"\nPlayer {player_num}, Please answer the following prompts to enter your demographic information")
    info = {}
    info['name'] = input("Name: ")
    while True:
        age_input = input("Age: ")
        if age_input.isdigit():
            info['age'] = int(age_input)
            break
        else:
            print("Please enter a valid number for age: ")
    info['city'] = input("City: ")
    print(info)
    return info

# 3) Collect items + metadata 
##Each player is to enter a minimum of three items.
### Each item = a dictionary with two metadata fields.

def input_collection(player_name):
    print(f"\n{player_name}, enter three items in your collection." )
    collection = {}
    for i in range(1):
        item = input(f"Item {i+1} name of your colleciton (example games, toys, food): ").strip().lower()
        meta1 = input("  Player input Item #1 : ")
        meta2 = input("  Player input Item #2 : ")
        meta3 = input("  Player input Item #3 : ")
        collection[item] = {"Item 1": meta1, "Item 2": meta2, "Item 3": meta3}
    return collection

# 4) Guessing game loop
## Players guess items from each other’s collection.
### Track number of guesses and scores.

def guessing_game(collection1, collection2, player1, player2):
    score1 = score2 = 0
    max_guesses = 3
    print("\nLet the guessing begin! ")
    
    for turn in range(max_guesses):
        print(f"\n--- Turn [turn+1 ---")
        #print(collection2)  # JUST CHECKING the data input to collection2 
        guess1 = input(f"{player1['name']}, guess an item from {player2['name']}'s collection: ").lower()
        #print(guess1) # JUST CHECKING THE VALUE REGISTRED AT variable guess1
        
        all_values = [v.lower() for item in collection2.values() for v in item.values()] #converting dictonary info to a list[]
        
        print(all_values)

        if guess1 in all_values:
            print("Correct!")
            score1 += 1
            #del collection2[guess1]
            
        else:
            print("Incorrect.")
        print(collection1)  # JUST CHECKING the data input to collection1
        guess2 = input(f"{player2['name']}, guess an item from {player1['name']}'s collection: ").lower()
        print(guess2)
        all_values = [v.lower() for item in collection1.values() for v in item.values()] #converting dictonary info to a list[]
        
        if guess2 in all_values:
            print("Correct!")
            score2 += 1
            #del collection1[guess2]
        else:
            print("Incorrect.")

        if not collection1 or not collection2:
            break

    print(f"\nFinal Score: {player1['name']} - {score1}, {player2['name']} - {score2}")

# 5) Scoring and ending


# MAIN POGRAM : 

display_welcome()
player1 = collect_player_info(1)
#print(player1)   #reviewing dictionary=player1 data 

player2 = collect_player_info(2)
#print(player2)   #reviewing dictionary=player2 data 

collection1 = input_collection(player1['name'])
#print(collection1)   #reviewing dictionary=collection1 data 

collection2 = input_collection(player2['name'])
#print(collection2)   #reviewing dictionary=colleciton2 data 

guessing_game(collection1, collection2, player1, player2)





