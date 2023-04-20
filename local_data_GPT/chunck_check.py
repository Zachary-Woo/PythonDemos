import spacy
from sklearn.metrics.pairwise import cosine_similarity

# Load the spaCy language model
nlp = spacy.load("en_core_web_md")

# Define a function to get embeddings of a given text
def get_embedding(text):
    return nlp(text).vector

# Define a function to find the most similar chunks to the given question
def find_similar_chunks(question, data_list):
    # Get the embedding of the question
    question_embedding = get_embedding(question)
    # Get the embeddings for each chunk in the data list
    embeddings = [get_embedding(chunk) for chunk in data_list]

    # Calculate cosine similarities between the question and data list embeddings
    similarities = cosine_similarity([question_embedding], embeddings)[0]
    # Get the indices of the top 10 most similar chunks
    sorted_indices = similarities.argsort()[-10:][::-1]

    # Return the top 20 most similar chunks
    return [data_list[index] for index in sorted_indices]