# WEAT-Analysis-of-Human-and-Language-Model-Biases-in-Romanian

### Introduction 

Understanding how cultural and social biases appear in language is an important step in analyzing both human reasoning and the behavior of artificial intelligence models. Previous studies have shown that word embeddings and language models trained on human-written texts often inherit, amplify, or even invert human biases. However, most existing work evaluates these phenomena in English, leaving a gap in understanding how such biases manifest in other languages. In this project, we aim to examine whether the Word Embedding Association Test (WEAT), and its multilingual variant CA-WEAT, reveal measurable biases in Romanian, both in humans and in AI models.

### Approach

Our approach is based on four main steps:
- We selected word categories inspired by CA-WEAT and translated them into Romanian.
- We created a survey in which participants rated words from 1–7 based on perceived associations.
- We collected equivalent ratings from AI models.
- We used SpaCy embeddings for Romanian and compared WEAT bias scores with mean results from both our survey collected responses.


### Datasets

We began our approach by selecting the dictionary of target found in the data provided on Github by Corpus del Español REAL and translating the entire word list into Romanian preserving meaning and context. 

After preparing the Romanian version of the word sets, we designed a Google Forms survey in which participants rated each word on a Likert scale from 1 to 7. The survey was completed by 40 Romanian speakers of diverse ages, ensuring a broad range of perspectives. 

To evaluate the same set of words using AI language models, we created a standardized prompt and submitted it to publicly available free APIs such as ChatGPT, Gemini, NotebookLM, Meta AI, DeepSeek, and Perplexity AI. Each model provided numerical ratings for the same Romanian word lists, and these outputs were collected and stored in a CSV file for further analysis.  

We then cleaned and aligned the human survey CSV with the AI CSV, ensuring both datasets shared the same structure, word order, and rating format. This preprocessing step allowed us to load both files into Python seamlessly.

### Use of WEAT

WEAT works by measuring how closely different groups of words are associated with particular attributes inside a word-embedding space. Each word is represented as a vector, and WEAT computes the cosine similarity between vectors to estimate how semantically related two words are. 

In our project, we apply WEAT to the entire word list using SpaCy embeddings imported in Python. For each word, we compute its association with the "pleasant" and "unpleasant" attribute sets. The results are stored in a dataframe of the form:(word, WEAT score to "unpleasant", WEAT score to "pleasant").
This dataframe is then sorted by highest association scores to generate the top 25 pleasant and top 25 unpleasant words. Finally, the sorted lists are saved as CSV files for further analysis and observation.

### Survey Interpretation

We processed human survey data and language model ratings to identify the most pleasant and unpleasant words. For each CSV file, we computed the mean rating of every word across all respondents or model outputs. The words were then sorted by these mean scores to extract the top 25 pleasant and top 25 unpleasant words. The results were saved in formatted text files, including word rank and mean score.

### Results

We observed all resulting files and outputs and compared the following:

**Top 25 pleasant words determined by SpaCy WEAT scores and by the human/language model surveys.**

The top results are “placere” for WEAT, “loial” for the human survey and “mângâiere” for the model survey; different words, but all within the same semantic category. Out of the 25 words in the human survey top list, 11 words (44\%) also appear in the WEAT top list, indicating a moderate overlap. Out of the 25 words in the language model top list, 14 words (56\%) also appear in the WEAT top list, showing a higher alignment compared to the human survey. Comparing the two surveys, 20 words are in common, corresponding to a 80\% similarity, indicating strong agreement between human judgments and model predictions.

**Top 25 unpleasant words determined by SpaCy WEAT scores and by the human/language model surveys.**

The top results are “urât” for WEAT, “cancer” for the human survey and “abuz” for the model survey; different words, but all within the same semantic category. Out of the 25 words in the human survey top list, 9 words (36\%) also appear in the WEAT top list, indicating moderate overlap. Out of the 25 words in the language model top list, 10 words (40\%) also appear in the WEAT top list, showing slightly higher alignment. Comparing both surveys, 18 words are in common, corresponding to a 72\% overlap, indicating strong agreement.

<p>
  <img src="https://github.com/mariaxadina/WEAT-Analysis-of-Human-and-Language-Model-Biases-in-Romanian/blob/main/overlap_bar_chart.png" width="500"/>
</p>

### Conclusions

The findings from this study suggest that while embedding-based measures such as WEAT provide a useful approximation of human semantic associations, language models trained on Romanian texts tend to align more closely with human judgments than static embeddings alone. 

By comparing human survey results, language model outputs, and WEAT scores for pleasant and unpleasant words, we observed that WEAT captures general semantic trends, but language models show stronger alignment with human perceptions. The consistently high overlap between human and model surveys indicates that modern language models reflect human preferences more accurately, supporting the importance of human-centered evaluations when assessing biases in language models.

Future work could expand this study by increasing the size of the dataset and collecting survey responses from a larger group of participants. Additionally, experimenting with other embedding models could provide further insight into how different representations capture semantic associations and biases in Romanian.

#### Collaboration
This study was developed in collaboration with [Chera Alexandru-Gabriel](https://github.com/gabirelul).

### Bibliography/Resources
1. https://cereal-es.github.io/CEREAL/#data
2. https://aclanthology.org/2022.emnlp-main.133/
3. https://aclanthology.org/2024.naacl-long.204.pdf
4. https://www.diva-portal.org/smash/get/diva2:1621875/FULLTEXT01.pdf
5. https://github.com/cristinae/CA-WEAT/blob/main/data/CA-WEATv1.tsv

   
