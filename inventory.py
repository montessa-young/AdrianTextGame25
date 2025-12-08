# inventory.py

# Initialize an empty inventory dictionary
inventory = {}

def show_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
        print()

def add_item():
    item = input("Enter the name of the item to add: ").strip()
    try:
        quantity = int(input(f"Enter the quantity of {item}: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} {item}(s) to inventory.\n")

def remove_item():
    item = input("Enter the name of the item to remove: ").strip()
    if item not in inventory:
        print(f"{item} is not in inventory.")
        return
    try:
        quantity = int(input(f"Enter the quantity of {item} to remove: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    if quantity >= inventory[item]:
        del inventory[item]
        print(f"{item} removed from inventory.\n")
    else:
        inventory[item] -= quantity
        print(f"Removed {quantity} {item}(s) from inventory.\n")

def main():
    while True:
        print("Inventory Menu:")
        print("1. Show Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            print("Exiting inventory system.")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()




class Player:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.level = 1
        self.exp = 0

    def add_money(self, amount):
        self.money += amount
        print(f"{self.name} earned ${amount}! Total money: ${self.money}")

    def spend_money(self, amount):
        if amount > self.money:
            print("❌ Not enough money!")
            return False
        self.money -= amount
        return True

    def add_exp(self, amount):
        self.exp += amount
        print(f"{self.name} earned {amount} XP!")

        while self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print(f"🎉 LEVEL UP! {self.name} is now level {self.level}!")

    def stats(self):
        print("\n----- PLAYER STATS -----")
        print(f"Name: {self.name}")
        print(f"Money: ${self.money}")
        print(f"Level: {self.level}")
        print(f"XP: {self.exp}/100")
        print("------------------------\n")


# --------------------------
# MARKET SYSTEM WITH ARMOR & SHIELDS
# --------------------------
market_items = [
    # Swords
    {"name": "Wooden Sword",   "price": 20,  "level_required": 1},
    {"name": "Iron Sword",     "price": 75,  "level_required": 2},
    {"name": "Steel Sword",    "price": 150, "level_required": 3},
    {"name": "enchanted Sword",    "price": 400, "level_required": 5},

    # Armor
    {"name": "Leather Armor",  "price": 50,  "level_required": 1},
    {"name": "Iron Armor",     "price": 120, "level_required": 2},
    {"name": "Steel Armor",    "price": 250, "level_required": 3},
    {"name": "Dragon Armor",   "price": 600, "level_required": 5},

    # Shields
    {"name": "Wooden Shield",  "price": 30,  "level_required": 1},
    {"name": "Iron Shield",    "price": 100, "level_required": 2},
    {"name": "Steel Shield",   "price": 200, "level_required": 3},
    {"name": "enchanted Shield",   "price": 500, "level_required": 5},
]

def show_market(player):
    print("\n===== MARKET =====")
    for item in market_items:
        lock = "🔒 LOCKED" if player.level < item["level_required"] else "✅ UNLOCKED"
        print(f"{item['name']} - ${item['price']} (Level {item['level_required']}) {lock}")
    print("==================\n")

def buy_item(player, item_name):
    for item in market_items:
        if item["name"].lower() == item_name.lower():

            if player.level < item["level_required"]:
                print(f"❌ You must be level {item['level_required']} to buy this!")
                return

            if player.spend_money(item["price"]):
                print(f"🛒 You bought {item['name']} for ${item['price']}!")
            else:
                print("❌ Not enough money!")
            return

    print("❌ Item not found.")


# --------------------------
# Example Game Flow
# --------------------------
player = Player("Player1")

player.add_money(300)
player.add_exp(250)  # Levels up twice

player.stats()
show_market(player)

buy_item(player, "Wooden Sword")
buy_item(player, "Steel Armor")
buy_item(player, "Magic Shield")  # Not enough level yet

player.stats()
