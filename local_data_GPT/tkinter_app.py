import tkinter as tk
from tkinter import ttk
from openai_call import chatbot

conversation_history = []

def submit_question():
    question = question_entry.get()
    question_text.insert(tk.END, "User: " + question + "\n")
    question_entry.delete(0, tk.END)

    answer = chatbot(question, conversation_history)
    question_text.insert(tk.END, "AI: " + answer + "\n")

root = tk.Tk()
root.title("ChatGPT")
root.geometry("800x600")
root.configure(bg="#444654")

frame = ttk.Frame(root, padding="30")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

question_text = tk.Text(frame, wrap=tk.WORD, bg="#343541", fg="#FFFFFF", font=("Arial", 12))
question_text.grid(column=0, row=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=question_text.yview)
scrollbar.grid(column=2, row=0, sticky=(tk.N, tk.S))
question_text["yscrollcommand"] = scrollbar.set

question_entry = ttk.Entry(frame, font=("Arial", 12))
question_entry.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))

submit_button = ttk.Button(frame, text="Submit", command=submit_question)
submit_button.grid(column=1, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="#444654")
style.configure("TFrame", background="#444654")
style.configure("TEntry", fieldbackground="#343541", background="#343541", font=("Arial", 12))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=3)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=10)

root.mainloop()