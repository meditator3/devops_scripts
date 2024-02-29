# find the runner up score(the second highest score)
# the idea is to retain the one stage before updating the highest score from
# the  comparisons in the array

score_sheet = [3,7,6,4,12, 33,90,1]

def runner_up_score(n, score_sheet):
    highest = score_sheet[0] # comparing the first item on the list as the highest

    for i in range(1, n): # starts on index 1 since we gave highest the first value of the score sheet
        if highest < score_sheet[i]: # comparing which is highest
            runner_up = highest # retain the previous highest
            highest = score_sheet[i] # replacing highest accordingly
    return runner_up # return the second highest score

print(f"from the score sheet{score_sheet} => the runner up score is:{runner_up_score(len(score_sheet), score_sheet)} ")

