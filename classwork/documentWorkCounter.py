import os
import collections
import re

DIRECTORY = "original"
FILENAME = "speech.txt"
N = 100  # top N words

file_path = os.path.join(DIRECTORY, FILENAME)
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Lowercase and extract words (alphanumeric, 2+ chars)
words = re.findall(r'\b\w{2,}\b', text.lower())

counter = collections.Counter(words)
most_common = counter.most_common(N)

print(f"Top {N} words in {FILENAME}:")
for word, count in most_common:
    print(f"{word}: {count}")
