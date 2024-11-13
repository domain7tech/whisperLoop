import os
import random
from datetime import datetime


def create_empty_file(file_path):
    with open(file_path, 'w'):
        pass


class Dirbuilder:
    def __init__(self, file_path):
        self.file_path = file_path


    def process_file(self):
        # Open and read the input file
        with open(self.file_path, 'r') as file:
            lines = file.readlines()


        # Write the modified content back to the input file
        with open(self.file_path, 'w') as file:
            file.writelines(lines)


        # Create a directory with the specified name format
        filename = os.path.basename(self.file_path)
        dir_name = (
            filename[:-4]
            + "_"
            + datetime.now().strftime("%Y%m%d")
            + "_"
            + str(random.randint(10000000, 99999999))
            + "_"
            + ''.join(random.choice('ABCDEFG') for _ in range(4))
        )


        os.makedirs(dir_name, exist_ok=True)

        self.dir_name = dir_name
        print(f"Created directory: {dir_name}")  # Print the name of the created directory


# Usage example:
# create_empty_file("xos.txt")
#
# file_processor = Dirbuilder("xos.txt")
# file_processor.process_file()
#
# #load new directory name for use in other areas of the program
# new_directory = file_processor.dir_name
# print(f"New directory name: {new_directory}") # Print the name of the new directory
#
# os.remove("xos.txt") # Delete the xos.txt file