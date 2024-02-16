# shopping_cart.py

class ShoppingCart:# represent a simple shopping cart
    def __init__(self):
        self.items = {} # initializes an empty dictionary name as items

    def add_item(self, item_name: object, quantity: object = 1) -> object:# add_item method

        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.items[item_name]

    def get_total(self):
        total = 0
        for item, quantity in self.items.items():
            # Assume price lookup logic here (e.g., from a database)
            total += quantity * 10  # Placeholder price
        return total


if __name__ == "__main__":
    # Example usage
    cart = ShoppingCart()
    cart.add_item("Apple", 5)
    cart.add_item("Banana")
    cart.add_item("Orange", 3)
    cart.add_item("Pear", 1)
    cart.add_item("Kiwi", 1)

    print(f"Items in cart: {cart.items}")
    print(f"Total cost: ${cart.get_total()}")
