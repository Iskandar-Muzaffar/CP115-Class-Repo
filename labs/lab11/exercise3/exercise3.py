target_points = int(input())

# Initialize variables
total_points = 0
rounds_played = 0

while total_points < target_points:
    round_points = int(input())
    total_points += round_points
    rounds_played += 1

# Print final results
print(total_points)
print(rounds_played)
