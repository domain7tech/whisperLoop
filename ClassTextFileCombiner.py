import os
import glob

class TextFileCombiner:
    def __init__(self, input_folder, output_folder, output_filename):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.output_filename = output_filename

    def combine_txt_files(self):
        # Create the output folder if it doesn't exist
        os.makedirs(self.output_folder, exist_ok=True)

        combined_txt = os.path.join(self.output_folder, self.output_filename)

        with open(combined_txt, 'w') as outfile:
            for txt_file in glob.glob(os.path.join(self.input_folder, '*.txt')):
                with open(txt_file, 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')

if __name__ == "__main__":
    input_folder = './docsbox/csv/calc/'
    output_folder = './docsbox/csv/calc/final/'
    output_filename = 'combined.txt'

    combiner = TextFileCombiner(input_folder, output_folder, output_filename)
    combiner.combine_txt_files()
