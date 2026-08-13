prices = [100, 250, 400, 1200, 50]
prices_with_gst = list(map(lambda price: price + (price * 18 / 100),prices))
print(prices)
print(prices_with_gst)
