# factorial

# nu = 1
# numb = int(input("Enter number:"))
# while numb<1:
#     nu = nu*(numb-1)
#     numb=numb-1
# print(nu)


# nu = int(input("enter a number: "))
# i =1
# v=1
# while i<=nu:
#    v=v*i
#    i=i+1
#
# print(v)
# nu1 = int(input("enter a number: "))
# nu2 = int(input("enter a number: "))
# nnn=1

# for i in range(0,5):
#     for j in range(0,5-i-1):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print("#",end=" ")
# print("


import os# st = ["test launch 3 writting some text \n","test launch 2 writting some text \n","test launch 1 writting some text \n"]

from itertools import islice

# fi = open("C:/Users/DELL/Desktop/sa.txt",'w')
# fi.writelines(st)
# print(fi.read())


# fi=open("C:/Users/DELL/Desktop/sa.txt",'r')
if os.path.exists("C:/Users/DELL/Desktop/sa.txt"):
    os.remove("C:/Users/DELL/Desktop/sa.txt")
    print("file deleted")
else:print("no file")