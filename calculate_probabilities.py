#!/usr/bin/env python3
import pandas as pd
import os
import pickle
import json

# Load the dataset
data_path = os.path.join(os.getcwd(), 'attached_assets', 'team_names_updated.csv')
df = pd.read_csv(data_path)

# Convert 'Hit Six' column to binary
df['Hit_Six'] = df['Hit Six'].apply(lambda x: 1 if x == 'Yes' else 0)

# Dictionary to store results
team_venue_probabilities = {}

# Calculate probabilities for each team and venue combination
for team in df['Team'].unique():
    team_venue_probabilities[team] = {}
    
    for venue in df['Venue'].unique():
        # Filter data for this team and venue
        team_venue_data = df[(df['Team'] == team) & (df['Venue'] == venue)]
        
        # Calculate probability of hitting a six
        if len(team_venue_data) > 0:
            six_probability = team_venue_data['Hit_Six'].mean()
        else:
            # If no data for this combination, use overall team average
            team_data = df[df['Team'] == team]
            if len(team_data) > 0:
                six_probability = team_data['Hit_Six'].mean()
            else:
                # If no data for this team, use overall average
                six_probability = df['Hit_Six'].mean()
        
        # Store probability
        team_venue_probabilities[team][venue] = six_probability

# Calculate team averages (for when venue-specific data is missing)
team_averages = {}
for team in df['Team'].unique():
    team_data = df[df['Team'] == team]
    if len(team_data) > 0:
        team_averages[team] = team_data['Hit_Six'].mean()
    else:
        team_averages[team] = df['Hit_Six'].mean()

# Calculate venue averages (for when team-specific data is missing)
venue_averages = {}
for venue in df['Venue'].unique():
    venue_data = df[df['Venue'] == venue]
    if len(venue_data) > 0:
        venue_averages[venue] = venue_data['Hit_Six'].mean()
    else:
        venue_averages[venue] = df['Hit_Six'].mean()

# Overall average (for when both team and venue data are missing)
overall_average = df['Hit_Six'].mean()

# Save all probabilities to a JSON file
probabilities = {
    'team_venue_probabilities': team_venue_probabilities,
    'team_averages': team_averages,
    'venue_averages': venue_averages,
    'overall_average': overall_average
}

with open('server/models/probabilities.json', 'w') as f:
    json.dump(probabilities, f, indent=2)

print("Probabilities calculated and saved to probabilities.json")

# Print some statistics
print(f"\nOverall six probability: {overall_average:.4f}")
print("\nTeam averages:")
for team, prob in sorted(team_averages.items(), key=lambda x: x[1], reverse=True):
    print(f"{team}: {prob:.4f}")

print("\nVenue averages:")
for venue, prob in sorted(venue_averages.items(), key=lambda x: x[1], reverse=True):
    print(f"{venue}: {prob:.4f}")

# Print some sample team-venue combinations
print("\nSample team-venue probabilities:")
for team in list(team_venue_probabilities.keys())[:3]:
    for venue in list(team_venue_probabilities[team].keys())[:3]:
        prob = team_venue_probabilities[team][venue]
        print(f"{team} at {venue}: {prob:.4f}")