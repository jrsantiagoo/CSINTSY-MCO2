"""
pinoybot.py

PinoyBot: Filipino Code-Switched Language Identifier

This module provides the main tagging function for the PinoyBot project, which identifies the language of each word in a code-switched Filipino-English text. The function is designed to be called with a list of tokens and returns a list of tags ("ENG", "FIL", or "OTH").

Model training and feature extraction should be implemented in a separate script. The trained model should be saved and loaded here for prediction.
"""

import re
import pickle
import numpy as np
from feature_conversion import *
from helpers import *
from typing import List

# Main tagging function
def tag_language(tokens: List[str]) -> List[str]:
    """
    Tags each token in the input list with its predicted language.
    Args:
        tokens: List of word tokens (strings).
    Returns:
        tags: List of predicted tags ("ENG", "FIL", or "OTH"), one per token.
    """
    # 1. Load your trained model from disk (e.g., using pickle or joblib)
    #    Example: with open('trained_model.pkl', 'rb') as f: model = pickle.load(f)
    #    (Replace with your actual model loading code)

    with open("pinoybot_rfc.pkl", 'rb') as f:
        model = pickle.load(f)

    # 2. Extract features from the input tokens to create the feature matrix
    #    Example: features = ... (your feature extraction logic here)

    features_li = []
    for i in tokens:
        features_li.append(create_features(i))
    # Convert into numpy array
    features = np.array(features_li)

    # 3. Use the model to predict the tags for each token
    #    Example: predicted = model.predict(features)

    predictions = model.predict(features)

    # 4. Convert the predictions to a list of strings ("ENG", "FIL", or "OTH")
    #    Example: tags = [str(tag) for tag in predicted]

    tags = [int_to_label(tag) for tag in predictions]

    # 5. Return the list of tags
    #    return tags

    return tags


if __name__ == "__main__":
    text = input()
    tokens = re.split(r'(\s+|,|\.|\?|!)', text)
    tokens = [token for token in tokens if token.strip()]
    print(tokens)
    print(tag_language(tokens))