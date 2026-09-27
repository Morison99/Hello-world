import os
os.system('cls')

file_name = "my_python_file.py"

a = file_name.find(".")
file_new_name = file_name[0:a]
# file_new_name = file_name.split(".")[0]
file_new_name2 = file_new_name.replace("_", " ")
print(file_new_name2.title())
