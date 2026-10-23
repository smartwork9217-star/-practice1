"""Inventory class
self.items: dict, name to (qty, price)
add_item(name, qty, price)
remove_item(name): KeyError "No item named ..." if
missing
total_value(): sum of qty x price
__len__: number of items
Main program
Read stock.txt with with open(); skip bad lines with a message
Print item count and total value
Remove "pen", print again; then remove "laptop" and catch the error"""

class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named '{name}'")
        del self.items[name]

    def total_value(self):
        return sum(qty * price for qty, price in self.items.values())

    def __len__(self):
        return len(self.items)

inv = Inventory()

with open("stock.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        if len(parts) == 3:
            name, qty_str, price_str = parts
            try:
                qty = int(qty_str)
                price = int(price_str)
                inv.add_item(name, qty, price)
            except ValueError:
                print(f"Skipping {name}: bad number")

print(f"{len(inv)} items, total value {inv.total_value()}")

inv.remove_item("pen")
print(f"{len(inv)} items, total value {inv.total_value()}")

try:
    inv.remove_item("laptop")
except KeyError as e:
    print(f"Error: {e}")