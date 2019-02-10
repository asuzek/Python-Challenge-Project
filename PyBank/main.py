# Modules
import os
import csv
fname="Instructions/PyBank/Resources/budget_data.csv"
# Set path for file
csvpath = os.path.join(fname)

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        print(row())
        # if row[0] == video:
        #     print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

        #     # BONUS: Set variable to confirm we have found the video
        #     found = True

        #     # BONUS: Stop at first results to avoid duplicates
        #     break

    # If the video is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
