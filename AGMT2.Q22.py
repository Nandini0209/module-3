#Write a Python program to check whether an element exists within a tuple.

TUPLE=(1,2,3,4,5,6,7,8,9)
print(TUPLE)
A=int(input("enter the value that u need to check:"))
if A in TUPLE:
    print("the value exists in the tuple")
else:
    print("the value does not exists in the tuple")
