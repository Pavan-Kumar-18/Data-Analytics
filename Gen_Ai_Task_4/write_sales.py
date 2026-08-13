file = open("sales_data.txt", "w")

sales = [1200, 450, 980, 1500, 3000]

for i in sales:
    data = str(i)
    file.write(data + "\n")
file.close()

readFile = open("sales_data.txt", "r")
print(readFile.read())
readFile.close()