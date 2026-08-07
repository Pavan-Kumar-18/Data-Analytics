
products = [
    "smartphones",
    "cotton kurtis",
    "wireless earbuds",
    "face serums",
    "phone cases",
    "running shoes"
]

categories = [
    "Electronics",
    "Clothing",
    "Electronics",
    "Beauty",
    "Accessories",
    "Footwear"
]

categories_set = set(products)
print(categories_set)
categories_set.add("Sports")
categories_set.add("Electronics") 
print(categories_set)
print("Beauty" in categories_set)
print(len(categories_set))