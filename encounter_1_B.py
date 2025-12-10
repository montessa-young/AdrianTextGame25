
import random
import time

# Player inventory for the trade system
player_inventory = {
    "gold": 10,
    "herbs": 0,
    "arrows": 0
}

def chance_encounter():
    encounters = ["shop", "bandits", "wolf"]
    encounter = random.choice(encounters)

    print(f"\n\n--- ENCOUNTER START ---")
    print(f"You encounter: {encounter.upper()}!")

    if encounter == "shop":
        shop()
    if encounter == "bandits":
        bandits()
    if encounter == "wolf":
        wolf()
    else:
        print(f"--- ENCOUNTER END ---")


def shop():
    """Handles meeting friendly rebels, including trading."""
    print("The shop ceeper greet you warmly and asks what supplies you would like.")

    while True:
        # Display current gold before asking for input
        print(f"\nYou currently have: {player_inventory['gold']} gold")
        choice = input("Do you want to TRADE or LEAVE? ").strip().lower()

        if choice == "trade":
            trade_with_shop()

        elif choice == "leave":
            print("You thank the shop ceeper and continue on your journey.")
            break

        else:
            print("The shop ceeper doesn't understand. Try typing TRADE or LEAVE.")


def trade_with_shop():
    """Simple trading menu with shop ceeper."""
    print("\n--- shop ---")
    print(f"You have: {player_inventory['gold']} gold")
    print("Items for sale:")
    print("1. Herbs (3 gold)")
    print("2. Arrows (2 gold)")
    print("3. Leave shop")

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
        print("You step away from the shop.")
        # We return here to exit the trade function and go back to the rebel_encounter while loop
        return

    else:
        print("Invalid choice.")

    print(f"Your inventory now: {player_inventory}")


def typing_challenge(context_word):
    """A quick time-based typing challenge used for fight or flight outcomes."""
    # Use a more descriptive list of words for the game
    words_to_type = [context_word, "quick", "escape", "action", "now"]
    TIMEOUT = 6  # seconds (made shorter to be challenging)

    print("\n--- ACTION CHALLENGE ---")
    print(f"Type the specified word as fast as you can! You have {TIMEOUT} seconds.")

    # We only run the challenge once per call
    word_to_type = random.choice(words_to_type)
    print(f"\nType this word: '{word_to_type}'")

    start_time = time.time()
    try:
        user_input = input("Your turn: ")
        end_time = time.time()
        time_taken = end_time - start_time

        # Check if the user's input is correct and within the time limit
        if user_input == word_to_type and time_taken < TIMEOUT:
            print(f"SUCCESS! You typed it in {time_taken:.2f} seconds.")
            return True # Indicates success
        else:
            print("\n--- FAILED CHALLENGE! ---")
            if user_input != word_to_type:
                print(f"You typed '{user_input}', but the word was '{word_to_type}'.")
            else:
                print(f"You took too long! You took {time_taken:.2f} seconds.")
            return False # Indicates failure
    except (KeyboardInterrupt, EOFError):
        print("\nChallenge abandoned.")
        return False


def bandits():
    """Handles any dangerous encounter (fight/run) using the typing challenge."""

    # Ensure choice input is clean
    choice = input(f"The bandits our sneeking down the hill towards you! Do you want to FIGHT or RUN? ").strip().lower()

    if choice == "fight":
        print(f"You stand your ground against the bandits!")
        # Run the typing challenge; 'fight' is the primary action word for the challenge
        if typing_challenge(context_word="fight"):
            print(f"\n>>> You manage to defeat the bandits! <<<")
            # Potential reward logic could go here
        else:
            print(f"\n>>> You where to slow you were killed. <<<")

    elif choice == "run":
        print(f"You try to escape from the bandits!")
        # Run the typing challenge; 'run' is the primary action word for the challenge
        if typing_challenge(context_word="run"):
            print(f"\n>>> You get away successfully! <<<")
        else:
            print(f"\n>>> You. <<<")

    else:
        print("Your hesitation gives you just enough time to back away and avoid danger.")

def wolf():
    """Handles any dangerous encounter (fight/run) using the typing challenge."""

    # Ensure choice input is clean
    choice = input(f"The farmer asks you to help with a wolf thats kills his lifestock. ! Do you want to FIGHT or run? ").strip().lower()

    if choice == "fight":
        print(f"You stand your ground against the wolf!")
        # Run the typing challenge; 'fight' is the primary action word for the challenge
        if typing_challenge(context_word="swing"):
            print(f"\n>>> You manage to defeat the wolf! <<<")
            # Potential reward logic could go here
        else:
            print(f"\n>>> You where to slow you were captured. <<<")

    elif choice == "run":
        print(f"You leave the farmer in distress!")


# This is the entry point for the script execution
if __name__ == "__main__":
    # Call the main game function to start an encounter
    chance_encounter()


















