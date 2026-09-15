"""
Program 9: Nest dictionaries – inventory of products with price and stock
Concept: Dictionaries (nesting, access, update)
"""

def demonstrate_nested_dictionary():
    """Demonstrate nested dictionaries with product inventory."""
    
    # Create nested dictionary for product inventory
    inventory = {
        "Laptop": {
            "price": 999.99,
            "stock": 15,
            "category": "Electronics"
        },
        "Mouse": {
            "price": 25.50,
            "stock": 50,
            "category": "Electronics"
        },
        "Keyboard": {
            "price": 75.00,
            "stock": 30,
            "category": "Electronics"
        },
        "Monitor": {
            "price": 299.99,
            "stock": 20,
            "category": "Electronics"
        }
    }
    
    print("Product Inventory:")
    print("=" * 50)
    
    # Display all products
    for product, details in inventory.items():
        print(f"Product: {product}")
        print(f"  Price: ${details['price']:.2f}")
        print(f"  Stock: {details['stock']} units")
        print(f"  Category: {details['category']}")
        print()
    
    # Access specific product information
    print("Accessing specific product info:")
    product_name = "Mouse"
    if product_name in inventory:
        product = inventory[product_name]
        print(f"{product_name}:")
        print(f"  Price: ${product['price']:.2f}")
        print(f"  Stock: {product['stock']} units")
    print()
    
    # Update stock after a sale
    print("Updating stock after sale:")
    product_to_sell = "Laptop"
    quantity_sold = 3
    
    if product_to_sell in inventory:
        inventory[product_to_sell]["stock"] -= quantity_sold
        print(f"Sold {quantity_sold} {product_to_sell}(s)")
        print(f"Remaining stock: {inventory[product_to_sell]['stock']} units")
    print()
    
    # Add new product
    print("Adding new product:")
    inventory["Headphones"] = {
        "price": 49.99,
        "stock": 25,
        "category": "Electronics"
    }
    print("Added Headphones to inventory")
    print(f"Headphones stock: {inventory['Headphones']['stock']} units")
    print()
    
    # Calculate total inventory value
    print("Calculating total inventory value:")
    total_value = 0
    for product, details in inventory.items():
        product_value = details["price"] * details["stock"]
        total_value += product_value
        print(f"{product}: ${details['price']:.2f} × {details['stock']} = ${product_value:.2f}")
    
    print(f"\nTotal inventory value: ${total_value:.2f}")

if __name__ == "__main__":
    demonstrate_nested_dictionary()