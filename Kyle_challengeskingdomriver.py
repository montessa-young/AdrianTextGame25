import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def backstory():
    print_slow("♘The Noble Knight was called by the king on a quest to retrieve the Great Dragons egg.")
    print_slow("However, the Knight will have to travel far and may encounter many threats along his way...")
    print_slow("Will the Noble Knight succeed with his quest or will he die on his way?")
    print_slow("⚔ Your actions will decide.")


backstory()






while True:
    import random
    import sys

    def hyper_simple_river_crossing():
        """
    Presents the traveler with the two main options and immediately delivers a result.
    Assumes the traveler starts with 10 gold.
    """

    BOAT_COST = 10
    gold = 50

    print("🌅 An old man by the river offers you a choice. You have 10 Gold Coins.")

    # --- Choices ---
    print("\n1. **Buy the Old Boat** (Cost: 10 Gold)")
    print("2. **Swim Across** (Free, 10% death risk, 30% item loss risk)")

    choice = input("\nEnter 1 or 2: ")

    # --- Decision Logic ---
    if choice == '1':
        # Buy the Boat
        if gold >= BOAT_COST:
            gold_left = gold - BOAT_COST
            print(f"\n✅ You bought the boat and safely crossed the river. You have {gold_left} gold left.")
            break

        else:
            print("\n❌ You don't have enough gold for the boat. No crossing today.")

    elif choice == '2':
        # Swim for Free (Risky)
        print("\n🌊 You attempt the swim...")

        risk_roll = random.random()

        if risk_roll < 0.10: # 10% Death
            print("\n💀 **DEATH.** The current was too strong. Your journey ends.")
            break
        elif risk_roll < 0.30: # 30% Item Loss (assuming you lose 1 gold)
            gold_lost = 1
            gold_left = gold - gold_lost
            print(f"\n⚠️ You are swept back to the shore, losing {gold_lost} gold in the process. You didn't cross.")
            print(f"You have {gold_left} gold remaining.")


        else: # 60% Success
            print("\n✅ **SUCCESS!** You made it across, soaked but safe.")
            break

    else:
        print("\n❓ Invalid choice. The old man shrugs and you stand still.")


print(hyper_simple_river_crossing())


