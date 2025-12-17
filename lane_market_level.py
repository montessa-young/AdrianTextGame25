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

def show_market():
    print("\n===== MARKET =====")
    for item in market_items:
        print(f"{item['name']} - ${item['price']}")
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


