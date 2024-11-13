import os
import pdfplumber

def pdf_to_text(pdf_path, output_txt_path):
    with pdfplumber.open(pdf_path) as pdf:
        with open(output_txt_path, 'w', encoding='utf-8') as output_file:
            for page in pdf.pages:
                text = page.extract_text()
                if text:  # Ensure there is text to write
                    output_file.write(text + '\n')

if __name__ == "__main__":
    pdf_directory = "./docsbox/pdf/"
    output_directory = "./docsbox/txt/"

    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through every file in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, filename)
            output_txt_path = os.path.join(output_directory, filename.rsplit('.', 1)[0] + '.txt')
            pdf_to_text(pdf_path, output_txt_path)
