# Q2.py

# correct function declaration and called from main program
# appropriate check digit determination algorithm (using modulo arithmetic) [2]
# function returns full bowler ID with check digit (not just check digit)
# appropriate generation of bowler ID (eg using random number generator)
# loop to process 10 bowler IDs
# 10 bowler IDs generated and written to text file (ensure uniqueness)
# open file in appropriate mode (write) and close file
# exception handling for file input/output (appropriate and specific error message)
# good programming style (meaningful identifier names, appropriate use of white space, appropriate comments)

import random

# declare global constants
NUM_BOWLERS = 10

# declare global variables
existing_bowlers = []   # list to store unique bowler IDs
num = 0

def UpdateID(bowler):
    """
      Function to calculate check digit and return full bowler ID
    """
    # initialize weights
    weights = [1, 3, 6, 7]
    # initialize sum of products
    sum_of_products = 0
    # loop to compute sum of products
    for i in range(len(bowler)):
        sum_of_products += int(bowler[i]) * weights[i]
    # calculate modulo arithmetic
    check_digit = sum_of_products % 10
    return bowler + str(check_digit)

# main
try:
    # open bowler file for output
    bowler_file = open("BOWLER.DAT", 'w')

    num = 0
    while num < NUM_BOWLERS:
        # generate random bowler ID from 1 to 9999
        bowler = random.randint(1, 9999)
        # zero pad from 0001 to 9999
        bowler = str(bowler).zfill(4)
        # get full bowler ID with check digit
        bowler = UpdateID(bowler)
        if bowler not in existing_bowlers: # ensure uniqueness
            # add to current bowlers
            existing_bowlers.append(bowler)
            # output to bowler ID file
            bowler_file.write(bowler + "\n")
            # next bowler ID
            num += 1

    # close bowler file
    bowler_file.close()
except IOError:
    # error message for file write
    print("Error writing to BOWLER.DAT.")