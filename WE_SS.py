#Word Embeddings Semantic Search
import pandas as pd
import spacy
from sklearn.metrics.pairwise import cosine_similarity

# Load the spaCy language model
nlp = spacy.load("en_core_web_md")

# Define a function to get word embeddings
def get_embedding(sentence):
    return nlp(sentence).vector

earnings_df = pd.read_csv('**** ENTER YOUR .csv FILE HERE (make sure you have the right file path!! ****')

earnings_df['embedding'] = earnings_df['text'].apply(get_embedding)
earnings_df.to_csv('**** ENTER THE FILE NAME TO SAVE THE EMBEDDINGS TO .csv ****')

earnings_search = input("Search earnings for a sentence:")
earnings_search_vector = get_embedding(earnings_search)

# You need to reshape the vectors before calculating cosine similarity
earnings_df["similarities"] = earnings_df['embedding'].apply(lambda x: cosine_similarity(x.reshape(1, -1), earnings_search_vector.reshape(1, -1))[0][0])

# Sort and display the top 10 results
sorted_earnings_df = earnings_df.sort_values("similarities", ascending=False)
print(sorted_earnings_df.head(10))
