#!/usr/bin/env python3
import pickle
import os
import sys
import numpy as np

# Path to the model file
MODEL_PATH = os.path.join(os.getcwd(), 'attached_assets', 'model.pkl')

def inspect_model():
    """Inspect the model structure."""
    try:
        print(f"Loading model from: {MODEL_PATH}")
        
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        
        print(f"Model type: {type(model)}")
        print(f"Model shape: {model.shape}")
        print(f"Model data type: {model.dtype}")
        
        # Display the first few values
        print(f"First 10 values: {model[:10]}")
        
        # Calculate some basic statistics
        print(f"Min value: {np.min(model)}")
        print(f"Max value: {np.max(model)}")
        print(f"Mean value: {np.mean(model)}")
        
        return True
    except Exception as e:
        print(f"Error inspecting model: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    inspect_model()