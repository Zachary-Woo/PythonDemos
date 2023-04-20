import csv
import docx
import os
import pickle
import PyPDF2

current_dir = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(current_dir, "data")
pickle_file_name = "preprocessed_data.pkl"

def save_to_pickle(data_list):
    with open(pickle_file_name, 'wb') as file:
        pickle.dump(data_list, file)

def load_from_pickle():
    with open(pickle_file_name, 'rb') as file:
        return pickle.load(file)

def read_data_files():
    if os.path.exists(pickle_file_name):
        return load_from_pickle()

    data_list = []

    for filename in os.listdir(data_directory):
        file_path = os.path.join(data_directory, filename)
        file_ext = os.path.splitext(filename)[-1].lower()

        if file_ext == ".csv":
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    data_list.append(" ".join(row))

        elif file_ext == ".docx":
            doc = docx.Document(file_path)
            for paragraph in doc.paragraphs:
                data_list.append(paragraph.text)

        elif file_ext == ".txt":
            with open(file_path, 'r', encoding='utf-8') as file:
                data_list.extend(file.readlines())

        elif file_ext == ".pdf":
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file) 
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    data_list.append(page.extract_text())

    save_to_pickle(data_list)

    return data_list