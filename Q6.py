#Write a Python program to read a file line by line and store it into a list

def read_file_into_list(tops.txt):
    lines = []
    try:
        with open("tops.txt", 'r') as file:
            for line in file:
                lines.append(line.strip())  # strip() removes the newline character at the end of each line
    except FileNotFoundError:
        print(f"Error: The file '{tops.txt}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines

filename = 'tops.txt'  
lines_list = read_file_into_list(tops.txt)
print(lines_list)
