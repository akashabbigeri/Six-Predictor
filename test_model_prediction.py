#!/usr/bin/env python3
import os
import sys
import numpy as np

# Add server directory to path so we can import from it
sys.path.append(os.path.join(os.getcwd(), 'server'))

# Import our predict function
from models.model_loader import predict_six_probability

# Test different team and venue combinations
teams = ['CSK', 'RCB', 'MI', 'KKR']
venues = ['Chennai', 'Bengaluru', 'Mumbai', 'Kolkata']

print("Testing model predictions with different team/venue combinations:")
print("-" * 50)

for team in teams:
    for venue in venues:
        result = predict_six_probability(team, venue)
        if 'error' in result:
            print(f"{team} at {venue}: ERROR - {result['error']}")
        else:
            print(f"{team} at {venue}: {result['probability']}% chance ({result['interpretation']})")

print("-" * 50)
print("Test complete!")