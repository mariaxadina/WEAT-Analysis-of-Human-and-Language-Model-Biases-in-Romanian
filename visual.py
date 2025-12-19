import matplotlib.pyplot as plt
import numpy as np


comparisons = [
    "Human vs WEAT",
    "Model vs WEAT",
    "Human vs Model"
]

pleasant = [44, 56, 80]
unpleasant = [36, 40, 72]

x = np.arange(len(comparisons))
width = 0.35

plt.figure(figsize=(8, 5))

plt.bar(x - width/2, pleasant, width, label="Pleasant words")
plt.bar(x + width/2, unpleasant, width, label="Unpleasant words")

plt.xticks(x, comparisons)
plt.ylabel("Overlap percentage (%)")
plt.xlabel("Comparison type")
plt.title("Overlap Between Human, Model, and WEAT Top-25 Word Lists")
plt.ylim(0, 100) 
plt.legend()

plt.tight_layout()
plt.savefig("overlap_bar_chart.png")
plt.show()
