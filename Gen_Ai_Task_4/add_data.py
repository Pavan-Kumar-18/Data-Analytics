file = open("sales_data.txt", "a")

file.write("5000\n")
file.write("2500\n")
file.write("1700\n")

file.close()

read = open("sales_data.txt", "r")

read_file = read.readlines()
count = len(read_file)
print(count)


read.close()