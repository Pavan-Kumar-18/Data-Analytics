import os

file_name = input("Enter file name: ")

avaliable = os.path.exists(file_name)

if avaliable:
    file = open(file_name, "r")
    data = file.readlines()
    for line in data:
        print(line.strip())
    file.close()
else:
    print("File not Exists")
