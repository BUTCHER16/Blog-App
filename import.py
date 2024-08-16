import itertools
from random import shuffle

# Define the teams
teams = ['Team A', 'Team B', 'Team C', 'Team D']

# Function to generate all possible matches in a round-robin format
def generate_round_robin_matches(teams):
    return list(itertools.combinations(teams, 2))

# Function to create a league schedule
def create_league_schedule(teams):
    all_matches = generate_round_robin_matches(teams)
    schedule = []
    
    # Shuffle to randomize match order
    shuffle(all_matches)
    
    # Initialize game counts
    games_played = {team: 0 for team in teams}
    
    # Add matches to schedule ensuring each team plays at least 3 games
    for match in all_matches:
        team1, team2 = match
        if games_played[team1] < 3 and games_played[team2] < 3:
            schedule.append(match)
            games_played[team1] += 1
            games_played[team2] += 1
            if all(games_played[team] >= 3 for team in teams):
                break
    
    return schedule

# Create the league schedule
schedule = create_league_schedule(teams)

# Print the schedule
print("League Match Schedule:")
for match in schedule:
    print(f"{match[0]} vs {match[1]}")

# Placeholder for rankings and finals determination
# Here you would include match results, compute standings, and determine the top 2 teams
print("\nTop 2 teams (example, needs real results):")
print("1. Team A")  # Example placeholder
print("2. Team B")  # Example placeholder
