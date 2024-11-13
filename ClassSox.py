import os
import subprocess
import shutil

class SoxProcessor:
    def __init__(self, target_directory, output_directory):
        self.target_directory = target_directory
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)

    def apply_sox_command(self, input_file, output_file):
        sox_command = ['sox', input_file, output_file, 'silence', '1', '0.1', '1%', '-1', '0.1', '1%']
        subprocess.run(sox_command)

    def process_files(self):
        for file_name in os.listdir(self.target_directory):
            if file_name.endswith('.mp3'):
                input_file = os.path.join(self.target_directory, file_name)
                fileprepend = "xos_"
                output_file = os.path.join(self.target_directory, fileprepend + file_name)

                self.apply_sox_command(input_file, output_file)

                shutil.copy(output_file, os.path.join(self.output_directory, fileprepend + file_name))

                os.remove(output_file)