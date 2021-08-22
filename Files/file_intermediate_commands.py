import os

# Program to demonstrate open and close function of file ...

# to open a file , here is the command  :-

open_file = open("new_file.txt", "wb")
#print("Name of file is : ", open_file.name)

# to close a opened file , Here is the command :-
open_file.close()

# -------------------------------------------------------------------------------

# to write content in a file what you want to , Here is the short program ,

open_a_file = open("new_file.txt", "w")
new_int = 8
# Write a content ...

# Additional i wrote a int variable and added it to file using format syntax ....
open_a_file.write("Here is the new item included in file ....{}".format(new_int))

# After writing something in file , Close opened file
open_a_file.close()

# --------------------------------------------------------------------------------

# Here we are reading a context in file ..
# to read what is in it , we have to execute the little program ..

read_a_file = open("new_file.txt", "r+")
read = read_a_file.read()
print(read)
read_a_file.close()

# ------------------------------------------------------------------------------

# To know the current position of file , use tell() method ..

know_position = open("new_file.txt", "r+")
read = know_position.read(6)
position = know_position.tell()
print(position)
know_position.close()
# ---------------------------

os.rename("sample.txt", "file2.txt")
os.rename("new_file.txt", "file.txt")
os.remove("sample.txt")