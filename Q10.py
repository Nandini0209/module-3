Write a Python program to count the frequency of words in a file.

from collections import Counter
import re

def count_word_frequency(tops.txt):
    word_count = Counter()
    try:
        with open(tops.txt, 'r') as file:
            for line in file:
                # Use regex to find words, ignoring punctuation and case
                words = re.findall(r'\b\w+\b', line.lower())
                word_count.update(words)
    except FileNotFoundError:
        print(f"Error: The file '{tops.txt}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return word_count

filename = 'tops.txt'
word_frequencies = count_word_frequency(tops.txt)
for word, count in word_frequencies.items():
    print(f"'{word}': {count} times")
