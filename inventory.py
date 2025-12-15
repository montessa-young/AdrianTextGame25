# inventory.py

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
            print("Not enough money!")
            return False
        self.money -= amount
        return True

    def add_exp(self, amount):
        self.exp += amount
        print(f"{self.name} earned {amount} XP!")

        while self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print(f" LEVEL UP! {self.name} is now level {self.level}!")

    def stats(self):
        print("\n----- PLAYER STATS -----")
        print(f"Name: {self.name}")
        print(f"Money: ${self.money}")
        print(f"Level: {self.level}")
        print(f"XP: {self.exp}/100")
        print("------------------------\n")


