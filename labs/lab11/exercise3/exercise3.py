target_points = int(input())

# Initialize variables
total_points = 0
rounds_played = 0

# Loop until total_points >= target_points
while total_points < target_points:
    points = int(input())  # Ask user for points
    total_points += points  # Add to total
    rounds_played += 1  # Count the round

# Print final results
print(total_points)
print(rounds_played)
