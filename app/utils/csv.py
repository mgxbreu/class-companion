def save_text(file_path, text):
    with open(file_path, "w") as text_file:
        text_file.write(text)

def read_text(file_path):
    with open(file_path, "r") as text_file:
        return text_file.read()