import pandas as pd
import numpy as np
import spacy
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

df_oameni = pd.read_csv("Human_based_Results.csv")
df_modele = pd.read_csv("Language_Models_Results.csv")

# 1 - foarte placut
# 7 - neplacut


def compute_mean_scores_transposed(csv_path):
    """
    Reads a CSV file where:
    - first row contains words
    - remaining rows contain numeric ratings

    Returns:
    - list of tuples (word, mean_score)
    """
    df = pd.read_csv(csv_path)

    results = []

    for word in df.columns:
        ratings = df[word].astype(float)
        mean_score = ratings.mean()
        results.append((word, mean_score))

    return results

human_scores = compute_mean_scores_transposed("Human_based_Results.csv")
model_scores = compute_mean_scores_transposed("Language_Models_Results.csv")

top25_pleasant_model = sorted(model_scores, key=lambda x: x[1], reverse=True)[:25]
top25_unpleasant_model = sorted(model_scores, key=lambda x: x[1])[:25]
top25_pleasant_human = sorted(human_scores, key=lambda x: x[1], reverse=True)[:25]
top25_unpleasant_human = sorted(human_scores, key=lambda x: x[1])[:25]


def save_top_to_txt(filename, top_list, title):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(title + "\n")
        f.write("=" * len(title) + "\n\n")
        for rank, (word, score) in enumerate(top_list, start=1):
            f.write(f"{rank:2d}. {word:<30s} {score:.3f}\n")

save_top_to_txt("top25_pleasant_human.txt", top25_pleasant_human, "Top 25 Most Pleasant Words (Human)")
save_top_to_txt("top25_unpleasant_human.txt", top25_unpleasant_human, "Top 25 Most Unpleasant Words (Human)")
save_top_to_txt("top25_pleasant_model.txt", top25_pleasant_model,"Top 25 Most Pleasant Words (Language Model)")
save_top_to_txt("top25_unpleasant_model.txt", top25_unpleasant_model, "Top 25 Most Unpleasant Words (Language Model)")
