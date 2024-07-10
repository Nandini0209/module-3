#Write a Python program to get unique values from a list .
U=[]
def function(x):
   for i in l:
       if i not in U:
          U.append(i)
   return U
l=[88,2,3,4,4,5,6,5,8]
print("the original list is:",l)
print("the new list is",function(U))
