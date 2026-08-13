

write_file = open("products.txt", "w")

for i in range(3):
    product_name = input("Enter Product Name: ")
    product_price = input("Enter Product Price: ")
    write_file.write(product_name +"|" + product_price+"\n")

write_file.close()

read_file = open("products.txt", "r")

read_data = read_file.readlines()

for line in read_data:
    print(line.strip())

read_file.close()