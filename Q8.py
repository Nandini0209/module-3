#Write a python program to find the longest words


def find_longest_words(tops.txt):
    longest_words = []
    max_length = 0
    try:
        with open(tops.txt, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word_length = len(word)
                    if word_length > max_length:
                        longest_words = [word]
                        max_length = word_length
                    elif word_length == max_length:
                        longest_words.append(word)
    except FileNotFoundError:
        print(f"Error: The file '{tops.txt}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return longest_words

# Example usage:
filename = 'tops.txt'  # replace with your filename
longest_words = find_longest_words(tops.txt)
print(f"The longest word(s) in the {tops.txt}' are: {longest_words}")
