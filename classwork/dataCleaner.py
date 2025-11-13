import os  # Import the os module for interacting with the operating system, like handling file paths
import re  # Import the re module for regular expressions, which we'll use for pattern matching in text

class TextProcessor:
    """
    This class is designed to process a text file by cleaning it up:
    - Removing specific filler words (like 'So', 'Actually', etc.)
    - Removing all line breaks and extra whitespace
    - Truncating the content to a maximum of 9000 characters
    - Saving the cleaned version to a new file
    
    It's useful for preparing speech transcripts or similar text data for further analysis or reading.
    """
    
    def __init__(self):
        """
        Constructor method: This is called when we create an instance of the TextProcessor class.
        It sets up the initial values (attributes) for the object, like file names and words to remove.
        """
        self.directory = "original"  # Directory where the input and output files are located (a folder named 'original')
        self.input_filename = "speech.txt"  # Name of the input file to read from (e.g., a speech transcript)
        self.output_filename = "cleaned_speech.txt"  # Name of the output file where cleaned text will be saved
        self.words_to_remove = [
            'So', 'so', 'Actually', 'Basically', 'Well', 'actually', 'basically',
            "Really", "really", "also"
        ]  # List of filler words to remove. Includes variations in capitalization for flexibility
        
        # Compile a regular expression pattern to match whole words (case-insensitive)
        # \b is a word boundary to ensure we match whole words only, not parts of other words
        # re.escape() is used to safely escape any special characters in the words
        # '|'.join() creates a pattern like 'So|so|Actually|...' for matching any of them
        # re.IGNORECASE makes the matching case-insensitive, so 'SO' would also match
        self.words_pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, self.words_to_remove)) + r')\b', re.IGNORECASE)

    def process_file(self):
        """
        Main method to process the file:
        1. Read the input file
        2. Clean the content (remove whitespace, line breaks, and specified words)
        3. Truncate to 9000 characters
        4. Write the cleaned content to the output file
        5. Print a confirmation message
        """
        # Create the full path to the input file by joining the directory and filename
        # This makes the code more portable across different operating systems
        input_path = os.path.join(self.directory, self.input_filename)
        
        # Create the full path to the output file similarly
        output_path = os.path.join(self.directory, self.output_filename)

        # Open the input file in read mode ('r') with UTF-8 encoding to handle special characters
        # 'with' statement ensures the file is properly closed after reading
        with open(input_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()  # Read the entire file content into a string

        # Remove all line breaks and whitespace:
        # file_contents.split() splits the string into a list of words (removing all whitespace)
        # ''.join() then joins them back into a single string with no spaces or newlines
        # This effectively concatenates all text into one continuous block
        file_contents = ''.join(file_contents.split())
        
        # Remove the specified words using the pre-compiled regex pattern
        # sub('') replaces matches with an empty string, effectively removing them
        file_contents = self.words_pattern.sub('', file_contents)
        
        # Truncate the string to the first 9000 characters
        # This prevents the file from being too large; if it's shorter, it remains unchanged
        file_contents = file_contents[:9000]

        # Open the output file in write mode ('w') with UTF-8 encoding
        # 'with' ensures it's closed properly; if the file doesn't exist, it's created
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(file_contents)  # Write the cleaned content to the file

        # Print a message to confirm the process is done and where the file is saved
        print(f"Cleaned file saved as {self.output_filename} in {self.directory}/")

# Usage
# This block runs only if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    tp = TextProcessor()  # Create an instance of the TextProcessor class
    tp.process_file()     # Call the process_file method to start the cleaning process
