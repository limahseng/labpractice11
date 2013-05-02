# Q3.py

# open files in appropriate modes (read and write) and close files
# sensible range for total number of games
# sensible range for score corresponding to total number of games
# 10 delimited records correctly written to text file

# appropriate use of data structures (eg list or dictionary)
# correct reading of variable length input records (eg using csv module or split() method)
# correct calculation of average score
# appropriate sort algorithm [2]
# correct determination of top 3 highest average scores [2]
# output of top 3 bowler IDs and scores
# formatting of average score to 1 or 2 decimal places
# cater to edge cases eg more than one top 3 average score

import csv
import random

# declare global variables
bowler_scores = {}
average_scores = []
highest1_bowler = []
highest2_bowler = []
highest3_bowler = []

def GenerateScores():
    try:
        # open delimited record files
        bowler_file = open("BOWLER.DAT", 'r', newline='')
        score_file = open("SCORES.DAT", 'w', newline='')

        records = csv.reader(bowler_file, delimiter=',')
        writer = csv.writer(score_file, delimiter=',')
        for record in records:
            # generate sensible games and score ranges
            num_games = random.randint(5, 10)
            total_score = random.randint(0, num_games * 300)
            writer.writerows([(record[0], str(num_games), str(total_score))])

        # close files
        bowler_file.close()
        score_file.close()
    except IOError:
        print("Cannot read from BOWLER.DAT or write to SCORES.DAT.")


def ComputeAverage():
    try:
        score_file = open("SCORES.DAT", 'r', newline='')

        records = csv.reader(score_file, delimiter=',')
        for record in records:
            bowler = record[0]
            num_games = int(record[1])
            total_score = int(record[2])
            average_score = total_score / num_games
            bowler_scores[bowler] = average_score
            average_scores.append(average_score)

        score_file.close()
    except IOError:
        print("Cannot read from SCORES.DAT.")
    return bowler_scores, average_scores


def BubbleSort(A):
    passes = len(A) - 1 # for n items, need n-1 passes
    swapped = True # assume not sorted
    while swapped:
        swapped = False
        i = 1
        while i <= passes:
            if A[i-1] < A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True
            i += 1
    passes -= 1
    return A


# main
GenerateScores()
bowler_scores, average_scores = ComputeAverage()
average_scores = BubbleSort(average_scores)
for bowler, average_score in bowler_scores.items():
    if average_score == average_scores[0]:
       highest1_bowler.append(bowler)
    if average_score == average_scores[1]:
       highest2_bowler.append(bowler)
    if average_score == average_scores[2]:
       highest3_bowler.append(bowler)
# output top 3 bowlers
for player in highest1_bowler:
    print("Top highest scorer is {0} with score {1:.2f}.".format(player, average_scores[0]))
for player in highest2_bowler:
    print("2nd highest scorer is {0} with score {1:.2f}.".format(player, average_scores[1]))
for player in highest3_bowler:
    print("3rd highest scorer is {0} with score {1:.2f}.".format(player, average_scores[2]))