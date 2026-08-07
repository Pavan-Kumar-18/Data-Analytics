
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Shirt", "category": "Clothing"},
    {"name": "Phone", "category": "Electronics"},
    {"name": "Jeans", "category": "Clothing"},
    {"name": "Apple", "category": "Food"},
]

price_dict = {
    "Laptop": 1200,
    "Shirt": 25,
    "Phone": 800,
    "Jeans": 50,
    "Apple": 2,
}

catalog = []
for prod in products:
    name = prod["name"]
    category = prod["category"]
    price = price_dict.get(name, 0)  
    catalog.append((name, price, category))

print("1. Catalog:", catalog)

category_to_products = {}
for name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(name)

print("\n2. Category to Products Mapping:", category_to_products)

max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))

print(f"\n3. Products in the largest category ({max_category}):")
for product_name in category_to_products[max_category]:
    print(f" - {product_name}")