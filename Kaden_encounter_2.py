import random
import time

# Player inventory for the trade system
player_inventory = {
    "gold": 10,
    "herbs": 0,
    "arrows": 0
}

def trade_with_fishing_villager_encounter():
    """Simple trading menu with fishing villager."""
    print("\n--- Fishing Villager Trading Post ---")
    # Use f-strings consistently for cleaner formatting
    print(f"You have: {player_inventory['gold']} gold")
    print("Items for sale:")
    print("1. Herbs (3 gold)")
    print("2. Arrows (2 gold)")
    print("3. Leave shop")

    # Use a try-except block for safer input handling
    try:
        choice = input("What would you like to buy? (1/2/3): ").strip()

        if choice == "1":
            if player_inventory["gold"] >= 3:
                player_inventory["gold"] -= 3
                player_inventory["herbs"] += 1
                print("You purchased 1 Herb.")
            else:
                print("You don’t have enough gold.")

        elif choice == "2":
            if player_inventory["gold"] >= 2:
                player_inventory["gold"] -= 2
                player_inventory["arrows"] += 1
                print("You purchased 1 Arrow.")
            else:
                print("You don’t have enough gold.")

        elif choice == "3":
            print("You step away from the trading post.")
            return # Exit the function

        else:
            print("Invalid choice.")
    except (KeyboardInterrupt, EOFError):
        print("\nInput error. Returning to village menu.")

    print(f"Your inventory now: {player_inventory}")


def fishing_village_encounter_handler():
    """Handles meeting friendly fishing villager, including trading."""
    print("The villagers greet you warmly and offer supplies.")

    while True:
        # Display current gold before asking for input
        print(f"\nYou currently have: {player_inventory['gold']} gold")
        # Ensure consistent input handling by stripping and lowercasing
        choice = input("Do you want to TRADE or LEAVE? ").strip().lower()

        if choice == "trade":
            trade_with_fishing_villager() # Correct function call
        elif choice == "leave":
            print("You thank the fishing villager and continue on your journey.")
            break
        else:
            print("The fishing villager doesn't understand. Try typing TRADE or LEAVE.")


def typing_challenge(context_word):
    """A quick time-based typing challenge used for fight or flight outcomes."""
    words_to_type = [context_word, "quick", "escape", "action", "now"]
    TIMEOUT = 4 # seconds

    print("\n--- ACTION CHALLENGE ---")
    print(f"Type the specified word as fast as you can! You have {TIMEOUT} seconds.")

    word_to_type = random.choice(words_to_type)
    print(f"\nType this word: '{word_to_type}'")

    start_time = time.time()
    try:
        # Use strip() to handle accidental spaces
        user_input = input("Your turn: ").strip()
        end_time = time.time()
        time_taken = end_time - start_time

        if user_input == word_to_type and time_taken < TIMEOUT:
            print(f"SUCCESS! You typed it in {time_taken:.2f} seconds.")
            return True
        else:
            print("\n--- FAILED CHALLENGE! ---")
            if user_input != word_to_type:
                print(f"You typed '{user_input}', but the word was '{word_to_type}'.")
            else:
                print(f"You took too long! You took {time_taken:.2f} seconds.")
            return False
    except (KeyboardInterrupt, EOFError):
        # Handle cases where user exits input
        print("\nChallenge abandoned.")
        return False


def swamp_goblin_encounter():
    """Handles dangerous encounter with a goblin (fight/run)."""
    choice = input(f"The swamp goblin is coming down the path towards you! Do you want to FIGHT or RUN? ").strip().lower()

    if choice == "fight":
        print(f"You stand your ground against the swamp goblin!")
        if typing_challenge(context_word="fight"):
            print(f"\n>>> You manage to defeat the swamp goblin! <<<")
        else:
            print(f"\n>>> You were too slow and were captured. <<<") # Fixed 'where' typo

    elif choice == "run":
        print(f"You try to escape from the swamp goblin!")
        if typing_challenge(context_word="run"):
            print(f"\n>>> You get away successfully! <<<")
        else:
            print(f"\n>>> You were too slow to escape and were captured. <<<")

    else:
        # Provide a default outcome for invalid input
        print("Your hesitation gives you just enough time to back away and avoid danger.")


def alligator_encounter():
    """Handles dangerous encounter with an alligator (fight/run)."""
    choice = input(f"You hear something in the water. It's an alligator! Do you want to FIGHT or RUN? ").strip().lower()

    if choice == "fight":
        print(f"You stand your ground against the alligator!")
        if typing_challenge(context_word="swing"):
            print(f"\n>>> You manage to defeat the alligator! <<<")
        else:
            print(f"\n>>> You were too slow and were defeated. <<<")

    elif choice == "run":
        print(f"You try to escape from the alligator!")
        if typing_challenge(context_word="run"):
            print(f"\n>>> You get away successfully! <<<")
        else:
            print(f"\n>>> You were not fast enough the alligator brings you under water. You Died. <<<")

    else:
        # Provide a default outcome for invalid input
        print("You were not fast enough the alligator brings you under water. You Died.")


def swamp_encounter():
    # Standardize all list items to lowercase for easy comparison
    # Added "small fishing village" to match the handler name better
    encounters = ["swamp goblin", "alligator", "small fishing village"]
    # Fixed typo: changed 'ramdom.chioce(encounters)' to 'random.choice(encounters)'
    encounter = random.choice(encounters)

    print(f"\n\n--- ENCOUNTER START ---")
    print(f"You encounter: {encounter.upper()}!")

    if encounter == "small fishing village":
        fishing_village_encounter_handler()
    elif encounter == "alligator":
        alligator_encounter()
    elif encounter == "swamp goblin":
        swamp_goblin_encounter()
    # No else block needed as all possibilities are covered in the list

    print(f"--- ENCOUNTER END ---")


# Added the missing function that was called in the __main__ block
def chance_encounter():
    """Wrapper function to initiate a random swamp encounter."""
    swamp_encounter()


# This is the entry point for the script execution
if __name__ == "__main__":
    # Call the main game function to start an encounter
    # This function call now works because 'chance_encounter' is defined above.
    chance_encounter()