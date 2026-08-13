def add_price( price_list):
    price = int(input("Enter Price: "))
    price_list.append(price)


def get_average_price(price_list):
    result = sum(price_list) / len(price_list)
    return result


def get_max_price(price_list):
    max = 0
    for i in price_list:
        if i > max:
            max = i
    return max


price_list = []
run = True
while(run):
    print(" 1. Enter the Price")
    print(" 2. Get Average Price")
    print(" 3. Get Max Price")
    print(" 4. Enter q to quit")
    user_input = input("Enter Choice: ")

    if user_input == "1":
        add_price(price_list)
    elif user_input == "2":
        print("Average Price", get_average_price(price_list))
    elif user_input == "3":
        print("Max Price: ",get_max_price(price_list))
    elif user_input == "q":
        print("Good Bye")
        run = False
    else:
        print("Invalid Choice Print Proper Choice")

