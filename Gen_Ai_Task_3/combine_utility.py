prices = [100, 500, 900, 50, 750]

def process_prices(prices):
    discount_prices = list(map(lambda price : price - price * 10 / 100, prices))
    filtered_prices = list(filter(lambda price : price > 300, discount_prices))
    return discount_prices, filtered_prices


print(process_prices(prices))