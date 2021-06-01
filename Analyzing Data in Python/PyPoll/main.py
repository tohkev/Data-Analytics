import os
import csv

path = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_list = []
vote_by_candidates = {}
candidate_rank = []
top_candidate = ""
vote_count = 0

with open(path, "r") as datafile:
    reader = csv.reader(datafile, delimiter=",")
    header = next(reader)

    for row in reader:

        # Counts the total amount of votes casted
        total_votes += 1

        # Creates a list of candidates by iterating
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

            # adds dictionary entry into vote_by_candidates if not there
            vote_by_candidates[row[2]] = 0

        vote_by_candidates[row[2]] += 1

    for key in vote_by_candidates.keys():
        if vote_by_candidates[key] > vote_count:
            top_candidate = key
            vote_count = vote_by_candidates[key]

    print(top_candidate, vote_count)
