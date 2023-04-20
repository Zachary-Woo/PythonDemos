import openai
from file_read import read_data_files
from chunck_check import find_similar_chunks
from chunck_check import nlp

# Set your OpenAI API key
openai.api_key = 'YOUR_OpenAI_API_Key'

# Define a function to ask GPT a question with the given data chunks
def ask_gpt(question, data_chunks, history):
    prompt = "Conversation history:\n"
    for interaction in history:
        prompt += f"User: {interaction['question']}\nAI: {interaction['answer']}\n"
    prompt += f"\nUser: {question}\n\nRelevant Data:\n"
    for chunk in data_chunks:
        tokens = nlp(chunk[:1000]) # Limit to 1000 characters
        short_chunk = " ".join([token.text for token in tokens[:100]])  # Limit to 100 tokens
        prompt += f"- {short_chunk}\n"
    prompt += "\nAnswer:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

# Define the main chatbot function
def chatbot(question, history):
    # Read data from files
    data_list = read_data_files()

    # Find the top 10 similar chunks
    similar_chunks = find_similar_chunks(question, data_list)

    # Get the answer from GPT-4
    answer = ask_gpt(question, similar_chunks, history)

    # Update history
    history.append({"question": question, "answer": answer})

    return answer

# Conversation history is outside of man due to need for it to be exported
conversation_history = []

# Main execution
if __name__ == "__main__":
    while True:
        question = input("Ask a question (type 'quit' to exit): ")
        
        if question.lower() == 'quit':
            break

        answer = chatbot(question, conversation_history)
        print(f"Answer: {answer}")
