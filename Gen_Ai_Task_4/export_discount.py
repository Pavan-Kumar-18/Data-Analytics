
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

user_discount = int(input("Enter Discount: "))
write_file = open("discount.txt", "w")

for key, price in prices.items():
    discount_amount = price - (price * user_discount / 100)
    write_file.write(key + '|'+ str(price) + "|" + str(discount_amount)+"\n")
write_file.close()

read_file = open("discount.txt", "r")

data = read_file.readlines()

for line in data:
    print(line.strip())
    
read_file.close()

