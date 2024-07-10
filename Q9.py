#Write a Python program to count the number of lines in a text file.

def count_lines_in_file(tops.txt):
    line_count = 0
    try:
        with open(tops.txt, 'r') as file:
            for line in file:
                line_count += 1
    except FileNotFoundError:
        print(f"Error: The file '{tops.txt}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return line_count

# Example usage:
filename = 'tops.txt'  # replace with your filename
num_lines = count_lines_in_file(tops.txt)
print(f"The file '{tops.txt}' has {num_lines} lines.")
