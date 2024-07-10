#Write a Python program to write a list to a file.

def write_list_to_file(tops.txt, data_list):
    try:
        with open(topstxt, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
filename = 'tops.txt'  # replace with your desired filename
data_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
write_list_to_file(tops.txt, data_list)
print(f"Data has been written to '{tops.txt}'")
