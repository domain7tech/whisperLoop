import os

class TextProcessor:
    def __init__(self, directory="./xos_main/txt/", words_to_remove=None):
        self.directory = directory
        self.words_to_remove = words_to_remove or ['So', 'so', 'Actually', 'Basically', 'Well', 'actually', 'basically', "Actually", "Really", "really", "also"]

    def process_files(self):
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.directory, filename)
                with open(file_path) as f:
                    file_contents = f.read().rstrip("\n")

                file_contents = file_contents[:9000]  # truncate to 9000 characters

                with open(file_path, 'w') as f:
                    f.write(file_contents)  # write truncated text back to file

                with open(file_path, "r+") as file:
                    result = ''.join([line for line in file if not line.isspace()])
                    file.seek(0)
                    file.write(result)  # remove extra line breaks and write back to file

                with open(file_path, 'r') as file:
                    string_with_line_breaks = file.read()

                lines = string_with_line_breaks.splitlines()
                string_without_line_breaks = ''.join(lines)

                with open(file_path, 'w') as file:
                    file.write(string_without_line_breaks)  # write the modified string back to the file

                with open(file_path, 'r') as input_file:
                    file_contents = input_file.read()
                    for word in self.words_to_remove:
                        file_contents = file_contents.replace(word, '')  # Filter word list out

                with open(file_path, 'w') as output_file:
                    output_file.write(file_contents)  # write the modified contents back to the file

                print(f"{filename} processed")

