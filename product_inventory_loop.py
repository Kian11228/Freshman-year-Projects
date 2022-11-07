# product_inventory_loop.py

# Programmer: Kian Esmaeili
# Class: CSCI1301-HY3, Fall 2022
# Purpose: Track products and their prices

# Create list of products and thier corresponding prices

# make sure to remeber to write the pupose of thew code HERE!


# List of prodcts and thier prices
products = []
prices = []

# Take Product and its price from user
product = input("Name of product ('stop' to end): ")
while product != "stop":
    products.append(product)
    price = float(input("Price of the product: ")) 
    prices.append(price)
    product = input("Name of product ('stop' to end): ")
        
print("The product inventory:")      
print(products, prices) 

# 2
average_price = sum(prices) / len(products)
percent_increase = float(input("By what percentage do you want to increase the product prices? (0-100): "))
for i in range (0, len(prices)):
    if prices[i] <= average_price:
        prices[i] = prices[i] + (percent_increase / 100) * prices[i]

# 3
most_ex = max(prices)
index_price = prices.index(most_ex)
print("The most expensive product, " + products[index_price] + " which costs " + str(prices.pop(index_price)) + " Dollars will be removed.")
print("The product inventory after " + products.pop(index_price) + " is removed:")
print(products)
print(prices)

# 4
product_remove = input("Name of the product to remove from inventory ('stop' to end): ")
while product_remove != "stop":
    if product_remove not in products:
        product_remove = input("Plase enter a valid product: ")
    else:
        product_remove = products.index(product_remove) 
        prices.pop(product_remove) 
        print("The product inventory after " + products.pop(product_remove) + " is removed: ")
        print(products)
        print(prices)
        product_remove = input("Name of the product to remove from inventory ('stop' to end): ")

#5
print("Products and respective prices side by side: ")
print("Product\tPrice")
print("-------         -----")

for i in range(0, len(prices)):
    print(products[i] + "\t" + str(prices[i]))

        
 



