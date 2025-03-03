letter_to_number = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}


def outcome_score(my_choice, opp_choice):
    diff = (my_choice - opp_choice) % 3
    if diff == 0:
        return 3  # Draw
    elif diff == 1:
        return 6  # Win
    else:  # diff == 2
        return 0  # Loss

total_score = 0

with open('input.txt', 'r') as f:
    for line in f:
        opp_letter, my_letter = line.strip().split()
        opp_choice = letter_to_number[opp_letter]
        my_choice = letter_to_number[my_letter]
        shape_score = my_choice
        outcome = outcome_score(my_choice, opp_choice)
        round_score = shape_score + outcome
        total_score += round_score

print(total_score) #result 8933