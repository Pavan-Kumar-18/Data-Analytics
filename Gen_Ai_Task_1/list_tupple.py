products = ["smartphones", "cotton kurtis","wireless earbuds", "face serums", "phone cases", "running shoes"]
sample_product = ("Laptop", 55000, "Electronics")

print(products[1], products[-1])
products.append("shirts")
products.append("Jackets")
print(products)
product_list = list(sample_product)
product_list[1] = 60000
sample_product = tuple(product_list)
print(sample_product)
