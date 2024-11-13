import os
import pypandoc

class DocxToTxtConverter:
    def __init__(self, docx_directory, txt_directory):
        self.docx_directory = docx_directory
        self.txt_directory = txt_directory

    def docx_to_txt(self, docx_path, txt_path):
        output = pypandoc.convert_file(docx_path, 'plain', outputfile=txt_path)
        assert output == ""

    def convert_all_docx_in_directory(self):
        if not os.path.exists(self.txt_directory):
            os.makedirs(self.txt_directory)

        for file_name in os.listdir(self.docx_directory):
            if file_name.endswith('.docx'):
                docx_path = os.path.join(self.docx_directory, file_name)
                txt_path = os.path.join(self.txt_directory, os.path.splitext(file_name)[0] + '.txt')
                self.docx_to_txt(docx_path, txt_path)
            print("Class Complete")

#Replace with the path to your 'docx' directory and the path where you want to save the .txt files
docx_directory = './docsbox/docx/'
txt_directory = './docsbox/txt/'
#
converter = DocxToTxtConverter(docx_directory, txt_directory)
converter.convert_all_docx_in_directory()
