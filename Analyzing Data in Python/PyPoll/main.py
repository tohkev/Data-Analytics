import os
import csv

path = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_list = []
vote_by_candidates = {}
top_candidate = ""
vote_count = 0
candidate_ranks = []
lower_ranks = []

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

        # adds a vote to the candidate
        vote_by_candidates[row[2]] += 1

    while len(candidate_ranks) < len(candidate_list):
        for candidate in candidate_list:
            if candidate in candidate_ranks:
                pass
            elif vote_by_candidates[candidate] > vote_count and candidate:
                top_candidate = candidate
                vote_count = (vote_by_candidates[candidate])

        candidate_ranks.append(top_candidate)
        top_candidate = ""
        vote_count = 0

    print(candidate_ranks)
