# This function will be tested automatically.
# Do not change the function name or parameters.


"""
    items: A list of dictionaries, each representing a product with keys:
        - "name": str
        - "price": int
        - "category": str
    
    Returns:
        - List of names of affordable products (price < 500)
        - Set of unique categories
        - Dictionary of product name to price mapping
        - Generator expression converted to list of prices after applying 10% discount
"""

def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]
    
    # Write your code below this line

    # List Comprehension
    productsBelow500 = [item['name'] for item in items if item['price'] < 500]
    
    # Set Comprehension
    uniqueCategories = {item['category'] for item in items}
    
    # Dictionary Comprehension
    mappedDict = {item['name'] : item['price'] for item in items}
    
    # Generator Expressions, not clogging whole memory at once, iterable only once.
    discountedPricesGenerator = (item['price'] * 0.9 for item in items)
    discountedPrices = list(discountedPricesGenerator)
    
    return (productsBelow500, uniqueCategories, mappedDict, discountedPrices)
    
    
    
    
    