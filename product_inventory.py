# product_inventory.py

# Programmer: Kian Esmaeili
# Class: CSCI1301-HY3, Fall 2022
# Purpose: Track products and their prices

# Create list of products and thier corresponding prices

# Input the 1st product info
product = input("Name of product 1: ")
price = float(input("Price of the product: "))

# Add the first product informtion to the list
product_list = [product]
price_list = [price]
print()
print("Inventory after the 1st product is added to it:")
print(product_list, price_list)
print()

# Input the 2nd product info to add to the end of the list
product = input("Name of product 2 to add to the end: ")
price = float(input("Price of the product: "))

# Add the information of the 2nd product to the end of list
product_list.append(product)
price_list.append(price)
print()
print("Inventory after the 2nd product is added to the end:")
print(product_list, price_list)
print()

# input the 3rd product info to add aftter the 1st product in list
product = input("Name of product 3 to add after the 1st product:")
price = float(input("Price of the product: "))

# Add the information of the 3rd prouct to the end of list
product_list.insert(1, product)
price_list.insert(1, price)
print()
print("Inventory after the 3rd product is added after the 1st product:")
print(product_list, price_list)
print()

# input the 4th product info to add to 3rd position of the list
product = input("Name of product 4 to insert in position 3 of inventory: ")
price = float(input("Price of the product: "))

# Add the information of the 4th product to the end of list
product_list.insert(2, product)
price_list.insert(2, price)
print()
print("Inventory after the 4th product is added to position 3:")
print(product_list, price_list)
print()

# input the 5th product info to the end of the list
product = input("Name of product 5 to add to the end of the inventory: ")
price = float(int(input("Price of the product: ")))

# Add the information of the 5th prouct to the end of list
product_list.append(product)
price_list.append(price)
print()
print("Inventory after the 5th product is added to the end of inventory:")
print(product_list, price_list)
print()

# input percentage to increase the products price
print("By what percentage do you want to increase the product prices? (0-100):")
percent = float(input())
percent_increase = (percent / 100)

# Applying the percent entered to the list of prices
price_list1 = [price_list[0] * percent_increase, price_list[1] * percent_increase, price_list[2] * percent_increase, price_list[3] * percent_increase, price_list[4] * percent_increase]                                                      
final_list = [price_list1[0] + price_list[0], price_list1[1] + price_list[1], price_list1[2] + price_list[2], price_list1[3] + price_list[3], price_list1[4] + price_list[4]]         
print("Inventory after all the prices are increased by 5 percent:")
print(product_list, final_list)
print()

# Removing the name of the product entered by the user
remove = input("Name of the product to remove from inventory: ")
index_of_remove = product_list.index(remove)
final_list.pop(index_of_remove)
product_list.remove(remove)
print("Inventory after", remove, "is removed from the inventory:" )
print(product_list, final_list)
print()

# finding the average price of the products
average_price = sum(final_list) / len(product_list)
print("The average price of 4 products is", average_price)

print("Original inventory:")
print(final_list, product_list)
print()
print("Reversed inventory:")
final_list.reverse()
product_list.reverse()
print(final_list, product_list)
print()

# Finding the least expensive product and its price
least_expensive = min(final_list)
index_product = final_list.index(least_expensive)
product_least_expensive = product_list[index_product]
print("The least expensive product", product_least_expensive, "costs", least_expensive, "Dollars")
print()
print()
# Showing the products and their prices in a vertical format
print("Products and respective prices side by side:")
print("Product", "\tPrice")
print("-------", "\t-----")

print(product_list[0], "\t\t", final_list[0])
print(product_list[1], "\t\t", final_list[1])
print(product_list[2], "\t\t", final_list[2])
print(product_list[3], "\t\t", final_list[3])
print()
print("Have a nice day!")