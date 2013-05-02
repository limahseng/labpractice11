# Q1.py

# initialize highest score to appropriate value (eg 0 or negative integer)
# while loop to prompt for additional entry / for loop to ask for number of entries
# if statement to compare current score and highest score
# action to replace highest score with new highest score
# validation of bowler ID
# validation of score
# output correct highest bowler ID and score
# cater to edge cases - no entry, more than one highest score, etc.

import re

# declare global constants
MAX_ENTRIES = 10    # maximum number of entries

# declare global variables
highest_score = 0   # initial lowest highest score
highest_bowler = [] # store list of bowler IDs with current highest score
num = 0             # current number of entries
another = 'y'       # response for more entry

def ValidateScore():
    """
      Function to get and validate bowler score
    """
    valid_score = False # assume invalid score
    # loop until score is valid
    while not valid_score:
        # get score
        score = input("Enter score: ")
        if len(score) == 0: # presence check
            print("Empty input")
        elif not score.isdigit(): # data type check
            print("Score must be numeric.")
        elif not 0 <= int(score) <= 300: # range check
            print("Score must be between 0 and 300 inclusive.")
        else: # valid score
            valid_score = True
    return int(score)

def ValidateBowler():
    """
      Function to get and validate bowler ID
    """
    valid_bowler = False # assume invalid bowler ID
    # loop until bowler ID is valid
    while not valid_bowler:
        # get bowler ID
        bowler = input("Enter bowler ID: ")
        if len(bowler) == 0: # presence check
            print("Empty input")
        elif len(bowler) != 4: # length check
            print("Bowler ID must be exactly 4 digits.")
        elif not bowler.isdigit(): # data type check
            print("Bowler ID must be numeric.")
        else: # valid bowler ID
            valid_bowler = True
    return bowler

def ValidateAnother():
    """
      Function to get and validate whether there is more entry
    """
    # set up valid pattern
    more_pattern = re.compile("[yYnN]")
    valid_another = False # assume invalid response
    # loop until response is valid
    while not valid_another:
        # get response
        another = input("Another entry(y/n)? ")
        if len(another) == 0: # presence check
            print("Empty input")
        elif not more_pattern.match(another): # y or n
            print("Please enter y or n.")
        else: # valid response
            valid_another = True
    return another

# main
# while there is more entries under limit
while (num < MAX_ENTRIES) and (another.lower() == 'y'):
    # get and validate score
    score = ValidateScore()
    # get and validate bowler ID
    bowler = ValidateBowler()
    # check if better or equals highest score
    if score >= highest_score:
        # update highest score
        highest_score = score
        # if beats previous high score, clear previous bowler ID(s)
        if score > highest_score:
            highest_bowler = []
        # add to existing highest score bowler ID(s)
        highest_bowler.append(bowler)
    # next entry
    num += 1
    # prompt for additional entry
    another = ValidateAnother()

# output highest score bowler(s)
print("Highest bowler ID(s):")
for player in highest_bowler:
    print(player)
# output highest score
print("Highest score:", highest_score)