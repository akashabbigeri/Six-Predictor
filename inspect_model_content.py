#!/usr/bin/env python3
import pickle
import os
import numpy as np

# Path to the model file
MODEL_PATH = os.path.join(os.getcwd(), 'attached_assets', 'model.pkl')

def inspect_model_content():
    """Print the full content of the model array."""
    try:
        print(f"Loading model from: {MODEL_PATH}")
        
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        
        print(f"Model shape: {model.shape}")
        print(f"Model content:")
        
        # Print each element with its index
        for i, value in enumerate(model):
            print(f"  [{i}] {value}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_model_content()