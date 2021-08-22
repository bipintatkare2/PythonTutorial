# The os module of python provides interaction with the operating systems.
# We can do OS-Level Operations with the functions provided by os & os.path module

# For performing those operations , we have to import os module ...

import os

# For getting current working directory ,
cwd = os.getcwd()

# ----------------------------------------

# For changing directory ,

os.chdir("../")

print(cwd)

# ----------------------------------------

# For creating directory ,

# First , we have to create a var which declares path of directory
path = "C:/Users/admin/Python Advance Topics/Advance Functions/"

# Then , we have to create a dir var and declare with a name ...
directory = "Bipin"

# Then , join both var "path" & "directory" with the help of os.path.join() method
dir = os.path.join(path, directory)

# Run command to creat ea directory .
os.mkdir(dir)

# -----------------------------------------

# To list-out all files and folders present in the cwd ,

all_list = os.listdir("C:/Users/admin/Python Advance Topics/")

print(all_list)

# ------------------------------------------

# To remove files or folders from system ,

# This is for file remove activity
# First define filename with var

# First create file if it dosen't exist or just create variable with filename
filename = "sample.txt"

# First create dir if it dosen't exist or just create variable with dirname
dirname = "Bipin"

# Define system path which belongs to file
system_path = "C:/Users/admin/Python Advance Topics/Advance Functions/"

# Join both using below function ...
file_path = os.path.join(system_path, filename)
dir_path = os.path.join(system_path, dirname)

# Apply command os.remove(path) -- path is of file
os.remove(file_path)
os.remove(dir_path)

# Other commands are specified here to get to know about them

# To know about name of OS , use os.name()
# To know which OSError will get occur , use os.error() it returns <class OSError>
# To make changes in files (Read / Write - Mode), use os.popen(filename, mode)
# - It is similar to file.open() method , just difference is it provides you
# pipeline / Gateway to go to final destination .
# To close a file , use os.close() which is more similar to file.close()
# To rename your file/folder , use os.rename()
# To check whether file/folder exists or not , use os.path.exists("file_name")
# To know size of file in bytes, use os.path.getsize("file_name")
