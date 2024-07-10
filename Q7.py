#Write a Python program to read a file line by line store it into a variable.

def read_file_into_variable(tops.txt):
    content = ""
    try:
        with open("tops.txt", 'r') as file:
            for line in file:
                content += line  # Add each line to the content variable
    except FileNotFoundError:
        print(f"Error: The file '{tops.txt}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return content


filename = 'tops.txt'  
file_content = read_file_into_variable(tops.txt)
print(file_content)
