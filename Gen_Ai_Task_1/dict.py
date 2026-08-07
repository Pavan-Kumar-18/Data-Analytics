price_dict = {
    "smartphones": 25000,
    "cotton kurtis": 1200,
    "wireless earbuds": 3000,
    "face serums": 800,
    "phone cases": 500,
    "running shoes": 4500
}

print(price_dict)

price_dict["shirts"] = 1500
print(price_dict)
price_dict["smartphones"] = 28000
print(price_dict)

product = "phone cases"

if product in price_dict:
    del price_dict[product]
    print(f"{product} removed successfully")
else:
    print(f"{product} not found")

print(price_dict)
total = 0

for price in price_dict.values():
    total += price

average = total / len(price_dict)
print("Average Price:", average)
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Maximum Price Product:", max_product, price_dict[max_product])
print("Minimum Price Product:", min_product, price_dict[min_product])

