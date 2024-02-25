import random
import names


class voter:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr


class vote:
    def __init__(self, id):
        self.id = id


class candidate:
    def __init__(self, name, list_positions, id):
        self.name = name
        self.list_positions = list(list_positions)
        self.id = id


class position:

    def __init__(self, pos_name, pos_id, candidates):
        self.candidates_votes = {}  # I chose dictionary for the number of votes for each candidate because it's fast to search and get the results
        self.name = pos_name
        self.pos_id = pos_id
        self.active_candidate = set()  # I chose set for active candidates because I want just to know if the candidate is active or not
        # In case there is a tie between multiple candidates ,we remove other candidates and do one more round with the tied candidates
        for c in candidates:
            if self.name in c.list_positions:
                self.candidates_votes[c] = 0
                self.active_candidate.add(c)


def voting(pos, voters):
    dict_votes = {}  # I chose dictionary for the votes because it's fast to search whether the voter did vote or not
    # voter should be unique to ensure that voter didn't vote more than one time,so voter is the KEY
    # vote includes id for a candidate so it can be duplicated , vote is the VALUE
    num_voters_illegal = 0
    blank_votes = 0
    candidate_with_blank = set(pos.active_candidate)
    candidate_with_blank.add(-1)  # -1 value refers to a blank vote
    for voter_ in voters:
        if voter_ not in dict_votes.keys():
            if voter_.age < 18:
                num_voters_illegal += 1
                dict_votes[voter_] = -1
            else:
                select_vote = random.sample(candidate_with_blank, 1)[0]
                if select_vote != -1:
                    dict_votes[voter_] = vote(select_vote.id)
                    pos.candidates_votes[select_vote] += 1
                else:
                    dict_votes[voter_] = select_vote
                    blank_votes += 1

    print(f"This is the results for {pos.name} position :\n"
          f"The number of the voters who did vote is {len(voters) - num_voters_illegal - blank_votes}\n"
          f"The number of the blank votes is {blank_votes}\n"
          f"The number of the people who didn't vote because they are under 18 is {num_voters_illegal}\n"
          f"This is the number of the votes for each candidate:")
    max_votes = max(list(pos.candidates_votes.values()))
    for cand, votes in pos.candidates_votes.items():
        if cand in pos.active_candidate:
            print(cand.name + ' : ' + str(votes))
            if votes != max_votes:
                pos.active_candidate.remove(cand)
            else:
                pos.candidates_votes[cand] = 0
    if len(pos.active_candidate) == 1:
        print(
            f"The winner of the {pos.name} position is {next(iter(pos.active_candidate)).name} with {max_votes} votes\n")
    else:
        print(f"Draw!! let's do another round between the tied candidates\n")
        voting(pos, voters)


if __name__ == '__main__':
    voters = []  #I chose list for the voters because it ensures the order of the voters by their arriving time
    # I could choose queue for the voters because we want first arrived first served
    # and queue ensures that but I need the voters for another positions
    list_candidates = [] #I chose list for the candidates and positions because I just want to store them and iterate over them
    positions = []
    names_pos = ["President", "Minster of Education", "Minister of Economy"]
    names_cand = ["SAMEER", "ADAM", "AYA", "LAELA"]

    for i in range(50):
        voters.append(voter(names.get_full_name(), random.randint(16, 70), "Kafr Kanna"))
    for i in range(4):
        list_candidates.append(candidate(names_cand[i], set(random.sample(names_pos, random.randint(1, 3))), i + 1))

    for i in range(3):
        positions.append(position(names_pos[i], i + 1, list_candidates))

    for pos in positions:
        voting(pos, voters)
