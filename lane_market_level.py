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
        lock = "LOCKED" if player.level < item["level_required"] else "UNLOCKED"
        print(f"{item['name']} - ${item['price']} (Level {item['level_required']}) {lock}")
    print("==================\n")

def buy_item(player, item_name):
    for item in market_items:
        if item["name"].lower() == item_name.lower():

            if player.level < item["level_required"]:
                print(f"You must be level {item['level_required']} to buy this!")
                return

            if player.spend_money(item["price"]):
                print(f"🛒 You bought {item['name']} for ${item['price']}!")
            else:
                print("Not enough money!")
            return

    print("Item not found.")


# --------------------------
# Example Game Flow
# --------------------------
player = Player("Player1")

player.add_money(300)
player.add_exp(250)

player.stats()
show_market(player)

buy_item(player, "Wooden Sword")
buy_item(player, "Steel Armor")
buy_item(player, "Magic Shield")

player.stats()
