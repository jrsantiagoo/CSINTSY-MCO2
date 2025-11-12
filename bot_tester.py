from pinoybot import tag_language
import pandas as pd

if __name__ == "__main__":
    # Example usage
    data = pd.read_csv("all_english.csv")
    test_tokens = data['word'].to_list()

    predictions = tag_language(test_tokens)

    with open("test_predictions.csv", 'w') as f:
        for p in predictions:
            print(p, file=f)