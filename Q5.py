#Write a Python program to read last n lines of a file

def read_last_n_lines("tops.txt", n):
    try:
        with open("tops.txt", 'r') as file:
            lines = file.readlines()[-n:]
            for line in lines:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{tops.txt}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


filename = 'tops.txt'
n = 5
read_last_n_lines("tops.txt", n)
