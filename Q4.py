#Write a Python program to read first n lines of a file
def read_first_n_lines("tops.txt", n):
    try:
        with open("tops.txt", 'r') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{tops.txt}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = 'tops.txt'  
n = 5
read_first_n_lines("tops.txt", n)

print("*"*30)
