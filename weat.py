import pandas as pd
import numpy as np
import spacy
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

#  definition of categories 

WORDS = [
"săgeată", "bâtă", "pistol", "rachetă", "suliță", "topor", "pumnal",
"harpon","pistol", "sabie", "lamă", "dinamită", "secure", "mitralieră", "tanc",
"bombă", "armă de foc", "cuțit", "pușcă de vânătoare", "gaz lacrimogen",
"tun", "grenadă", "buzdugan", "praștie", "bici",

"aster", "trifoi", "zambilă", "gălbenele", "mac", "azalea", "brândușă",
"iris", "orhidee", "trandafir", "clopoțel", "narcisă", "liliac",
"panseluță", "lalea", "piciorul-cocoșului", "margaretă", "crin",
"bujor", "violetă", "garoafă", "gladiolă", "magnolie", "petunie",
"cârciumăreasă",

"cimpoi", "violoncel", "chitară", "lăută", "trombon", "banjo",
"clarinet", "muzicuță", "mandolină", "trompetă", "fagot", "tobă",
"harpă", "oboi", "tubă", "clopot", "scripcă", "clavecin", "pian",
"violă", "bongo", "flaut", "corn", "saxofon", "vioară",

"furnică", "omidă", "purice", "lăcustă", "păianjen", "ploșniță",
"centipedă", "muscă", "larvă", "tarantulă", "albină",
"gândac de bucătărie", "țânțar mic", "țânțar", "termită", "cărăbuș",
"greiere", "gărgăun", "molie", "viespe", "musculiță", "libelulă", "tăun", "gândac", "gărgăriță",

"mângâiere", "libertate", "sănătate", "iubire", "pace", "veselie",
"prieten", "rai", "loial", "plăcere", "diamant", "blând", "onest",
"norocos", "curcubeu", "diplomă", "cadou", "onoare", "miracol",
"răsărit", "familie", "fericit", "râs", "paradis", "vacanță",

"abuz", "accident auto", "murdărie", "crimă", "boală", "accident",
"moarte", "doliu", "otravă", "duhoare", "atac", "dezastru", "ură",
"poluare", "tragedie", "divorț", "arest", "sărăcie", "urât",
"cancer", "ucidere", "putred", "vomă", "agonie", "închisoare"
]


nlp = spacy.load("ro_core_news_lg")

negative_word = "neplăcut"
doc_negative = nlp(negative_word)

positive_word = "plăcut"
doc_positive = nlp(positive_word)

word_similarities = {}

for word in WORDS:
    doc_word = nlp(word)
    
    if doc_word.has_vector and doc_negative.has_vector and doc_positive.has_vector:
        sim_neg = doc_word.similarity(doc_negative)
        sim_pos = doc_word.similarity(doc_positive)

        word_similarities[word] = (sim_neg, sim_pos)
    else:
        word_similarities[word] = (None, None)


# > 0 → cuvintele sunt semantic apropiate
# ≈ 0 → aproape necorelate
# < 0 → cuvintele sunt semantic opuse în embedding space

for word, (sim_neg, sim_pos) in word_similarities.items():
    if sim_neg is not None and sim_pos is not None:
        print(f"{word:30s} -> neg: {sim_neg:.3f}, pos: {sim_pos:.3f}")
    else:
        print(f"{word:30s} -> neg: N/A, pos: N/A")

df_sim = pd.DataFrame.from_dict(
    word_similarities,
    orient="index",
    columns=["similarity_negative", "similarity_positive"]
)

df_sim.reset_index(inplace=True)
df_sim.rename(columns={"index": "word"}, inplace=True)

top25_positive = (
    df_sim
    .sort_values(by="similarity_positive", ascending=False)
    .head(25)
)

top25_negative = (
    df_sim
    .sort_values(by="similarity_negative", ascending=False)
    .head(25)
)

top25_positive.to_csv("top25_semantic_pleasant.csv", index=False, encoding="utf-8")
top25_negative.to_csv("top25_semantic_unpleasant.csv", index=False, encoding="utf-8")
