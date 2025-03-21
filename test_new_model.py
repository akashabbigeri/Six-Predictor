#!/usr/bin/env python3
import os
import sys
import pandas as pd

# Add the parent directory to the path so we can import from it
sys.path.append(os.getcwd())

# Import the model loader
from server.models.model_loader import predict_six_probability

# Define test cases
test_cases = [
    ('RCB', 'Bengaluru'),
    ('MI', 'Mumbai'),
    ('CSK', 'Chennai'),
    ('KKR', 'Kolkata'),
    ('RR', 'Jaipur'),
    ('DC', 'Delhi')
]

print("=" * 50)
print("Testing IPL Six Prediction Model")
print("=" * 50)

# Run test predictions
for team, venue in test_cases:
    print(f"\nPrediction for {team} at {venue}:")
    result = predict_six_probability(team, venue)
    
    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Probability: {result['probability']}%")
        print(f"Interpretation: {result['interpretation']}")
        
print("\n" + "=" * 50)
print("Test complete!")
print("=" * 50)