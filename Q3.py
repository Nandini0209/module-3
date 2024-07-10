#Write a Python program to append text to a file and display the text.
file=open("tops.txt",'a')
file.write("this is my page")
print(file.read())
file.close()
print("*"*30)
