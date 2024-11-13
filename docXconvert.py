import os
import pypandoc

def docx_to_txt(docx_path, txt_path):
    output = pypandoc.convert_file(docx_path, 'plain', outputfile=txt_path)
    assert output == ""

def convert_all_docx_in_directory(docx_directory, txt_directory):
    if not os.path.exists(txt_directory):
        os.makedirs(txt_directory)

    for file_name in os.listdir(docx_directory):
        if file_name.endswith('.docx'):
            docx_path = os.path.join(docx_directory, file_name)
            txt_path = os.path.join(txt_directory, os.path.splitext(file_name)[0] + '.txt')
            docx_to_txt(docx_path, txt_path)

docx_directory = './docsbox/docx/'  # Replace with the path to your 'docx' directory
txt_directory = './docsbox/txt/'   # Replace with the path where you want to save the .txt files

convert_all_docx_in_directory(docx_directory, txt_directory)
