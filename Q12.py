#Write a Python program to copy the contents of a file to another file.

def copy_file_contents(source_tops.txt, destination_filename):
    try:
        with open(source_tops.txt, 'r') as source_file:
            contents = source_file.read()
        
        with open(destination_tops.txt, 'w') as destination_file:
            destination_file.write(contents)
        
        print(f"Contents of '{source_tops.txt}' have been copied to '{destination_filename}'")
    except FileNotFoundError:
        print(f"Error: The file '{source_tops.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_filename = 'tops.txt'  # replace with your source filename
destination_filename = 'tops.txt'  # replace with your destination filename
copy_file_contents(source_filename, destination_filename)
