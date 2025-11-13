import os  # Import the os module for working with file paths and directories
import collections  # Import the collections module, which provides specialized container datatypes like Counter
import re  # Import the re module for regular expressions, used for pattern matching in strings

# Define constants for the directory and filename
# Using uppercase for constants is a common Python convention to indicate they shouldn't be changed
DIRECTORY = "original"  # The folder where the input file is located
FILENAME = "speech.txt"  # The name of the file containing the text (e.g., a speech transcript)
N = 100  # The number of top words to display; this is how many of the most frequent words we'll show

# Construct the full path to the file by joining the directory and filename
# os.path.join handles differences in path separators across operating systems (e.g., / vs \)
file_path = os.path.join(DIRECTORY, FILENAME)

# Open the file in read mode ('r') with UTF-8 encoding to handle special characters or accented letters
# The 'with' statement ensures the file is automatically closed after we're done, even if an error occurs
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()  # Read the entire contents of the file into a string variable called 'text'

# Now, process the text to extract words:
# - text.lower() converts the entire text to lowercase for case-insensitive counting (e.g., 'The' and 'the' are treated the same)
# - re.findall() finds all matches in the string based on the regex pattern
# - The pattern r'\b\w{2,}\b' means:
#   - \b: word boundary (ensures we match whole words, not parts of words)
#   - \w{2,}: one or more word characters (letters, digits, underscores), but at least 2 characters long
#   - \b: another word boundary
# This extracts words that are alphanumeric and at least 2 characters, ignoring single letters, punctuation, etc.
words = re.findall(r'\b\w{2,}\b', text.lower())

# Use collections.Counter to count the frequency of each word in the list
# Counter is like a dictionary where keys are words and values are their counts
counter = collections.Counter(words)

# Get the top N most common words and their counts
# most_common(N) returns a list of tuples: [(word1, count1), (word2, count2), ...] sorted by count descending
most_common = counter.most_common(N)

# Print a header message indicating what we're displaying
# f-strings (formatted strings) allow embedding variables directly in the string with {}
print(f"Top {N} words in {FILENAME}:")

# Loop through the list of most common words
# Each item in most_common is a tuple (word, count), which we unpack into variables 'word' and 'count'
for word, count in most_common:
    # Print each word and its count in the format "word: count"
    print(f"{word}: {count}")
