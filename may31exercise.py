ballots = [
    {'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
    {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
    {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
    {'gold': 'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
    {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
    {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}
    ]

# Each dictionary represents a voting ballot, with three names in gold, silver, and bronze tiers. 
# A 'gold' is worth 3 points, 'silver' is worth 2 points, and 'bronze' is worth 1 point.
# For example, the first ballot {'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'} 
# shows that this voter chose Smudge for first place, Tigger for 2nd, and Simba for 3rd. 
# Smudge would be awarded 3 points, Tigger would be awarded 2 points, and Simba would be awarded 1 point.
# Tally up all the votes and determine who won.

votes = {
    'Smudge': 0,
    'Tigger': 0,
    'Simba': 0,
    'Bella': 0,
    'Lucky': 0,
    'Boots': 0,
    'Felix': 0
    }

for ballot in ballots:
    for key, value in ballot.items():
        if key == 'gold':
            votes[value] += 3
        elif key == 'silver':
            votes[value] += 2
        elif key == 'bronze':
            votes[value] += 1
winner = max(votes, key=votes.get)
print(winner)