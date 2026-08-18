class Item:
    """A single item in the inventory."""
    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount: int) -> None:
        """Adjusts item stock level."""
        self.quantity += amount

    def get_total_value(self) -> float:
        """Total monetary value for this item stock."""
        return self.quantity * self.price

    def __str__(self) -> str:
        return f"[{self.item_id}] {self.name:<15} | Stock: {self.quantity:<4} | Price: ${self.price:.2f}"


class InventoryManager:
    """Manages collection of items and operations."""
    def __init__(self):
        self.inventory = {}

    def add_item(self, item: Item) -> None:
        """Adds a new item object to the inventory."""
        if item.item_id in self.inventory:
            print(f"Error: Item ID {item.item_id} already exists.")
        else:
            self.inventory[item.item_id] = item
            print(f"Added: {item.name}")

    def update_stock(self, item_id: str, amount: int) -> None:
        """Updates stock levels for an existing item."""
        if item_id in self.inventory:
            self.inventory[item_id].update_quantity(amount)
            print(f"Updated Stock for [{item_id}]: New Quantity = {self.inventory[item_id].quantity}")
        else:
            print(f"Error: Item ID {item_id} not found.")

    def display_inventory(self) -> None:
        """Displays all items in structured format."""
        print("\n--- Current Inventory Status ---")
        if not self.inventory:
            print("Inventory is empty.")
            return
        total_val = 0.0
        for item in self.inventory.values():
            print(item)
            total_val += item.get_total_value()
        print(f"Total Inventory Value: ${total_val:.2f}\n")


# --- Test Cases ---
if __name__ == "__main__":
    manager = InventoryManager()

    print("=== Test Case 1: Adding Initial Items ===")
    item1 = Item("INV001", "Arduino Uno", 15, 22.50)
    item2 = Item("INV002", "CT Sensor", 30, 8.75)
    manager.add_item(item1)
    manager.add_item(item2)
    manager.display_inventory()

    print("=== Test Case 2: Updating Stock Levels ===")
    manager.update_stock("INV001", 5)   # Stock increases to 20
    manager.update_stock("INV002", -10)  # Stock decreases to 20
    manager.display_inventory()

    print("=== Test Case 3: Error Handling & Adding Duplicate ID ===")
    duplicate_item = Item("INV001", "Duplicate Microcontroller", 5, 10.00)
    manager.add_item(duplicate_item)
    manager.update_stock("INV999", 5)  # Non-existent ID test