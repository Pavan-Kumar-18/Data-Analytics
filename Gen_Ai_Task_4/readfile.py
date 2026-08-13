file = open("sales_data.txt", "r")

readFile = file.read()
print("Read File",readFile)
file.seek(0)

read_file_lines = file.readline()
print("Read File Lines",read_file_lines)

sale_list =[]

read_file_line = file.readlines()
for i in read_file_line:
    sale_list.append(int(i.strip()))

print(sale_list)
file.close()