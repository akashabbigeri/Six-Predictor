#!/usr/bin/env python3
import pickle
import os
import sys

# Path to the model file
MODEL_PATH = os.path.join(os.getcwd(), 'attached_assets', 'model.pkl')

def test_model_loading():
    """Test if the model can be loaded successfully."""
    try:
        print(f"Attempting to load model from: {MODEL_PATH}")
        print(f"File exists: {os.path.exists(MODEL_PATH)}")
        
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        
        print("Model loaded successfully!")
        print(f"Model type: {type(model)}")
        
        # Try to get some information about the model
        try:
            if hasattr(model, 'feature_names_in_'):
                print(f"Model features: {model.feature_names_in_}")
            elif hasattr(model, 'feature_names'):
                print(f"Model features: {model.feature_names}")
        except Exception as e:
            print(f"Could not retrieve feature names: {e}")
        
        return True
    except Exception as e:
        print(f"Error loading model: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    test_model_loading()