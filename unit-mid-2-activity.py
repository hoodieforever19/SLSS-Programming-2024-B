#Unit mid 2 activity
#Derek Nong
#June 19th 2024

def isfruitstock(fruit, stock):
    """
    Check if a fruit is in stock
    Params:
        fruit: The name of the fruit to check
        stock: A list of fruits that are in stock
    Returns:
        True if the fruit is in stock, False otherwise
    """
    return fruit in stock

# List of fruits in stock
fruits_in_stock = ["apple", "banana", "orange", "grape", "kiwi"]

# List of fruits to check
fruits_to_check = ["apple", "cherry", "kiwi", "mango"]

# Check availability of each fruit
for fruit in fruits_to_check:
    in_stock = isfruitstock(fruit, fruits_in_stock)
    if in_stock:
        print(f"The fruit {fruit} is in stock.")
    else:
        print(f"The fruit {fruit} is not in stock.")
