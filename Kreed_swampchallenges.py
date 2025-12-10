import time
import random

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)
    print()

def swampchallenges():
    print_slow("As the sun begins to set you decide to make shelter for the night.")
    print_slow("Do you either, (tree) make camp under a tree, (ground) make camp on the ground, or (willows) make shelter under the willows.")

swampchallenges()

def decide_campsite():
    """
    Prompts the user for a campsite choice and introduces a chance system for outcomes.
    """
    print("Where would you like to set up camp?")
    print("Options: 'tree', 'ground', or 'willows'")
    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -")

    # Get user input
    user_choice = input("Enter your choice here: ").lower().strip()

    # Determine outcome based on a 10% chance to die
    chance = random.random() # Generates a number between 0.0 and 1.0

    if chance < 0.10: # 10% chance (0.0 to 0.1)
        print("\n💀 A deadly snake attacks in the night! You have died.")
    elif chance > .10:
        print("You have succesfully surivied the night.")
    else:  # 90% chance (0.1 to 1.0)
        # Evaluate the user's choice using if/elif/else for the 'survive' scenarios
        if user_choice == "tree":
            print("\nDecision: Making camp under a tree.")
        elif user_choice == "ground":
            print("\nDecision: Making camp on the ground.")
            print("🌠 You sleep on the ground and you sleep peacefully during the night.")
        elif user_choice == "willows":
            print("\nDecision: Making camp under the willows.")
            print("🦅 You sleep underneath the willows and a bird attacks you!")
        else:
            # Handles any input that doesn't match the valid options
            print(f"\n'{user_choice}' is not a valid option.")
            print("Please restart the program and choose either 'tree', 'ground', or 'willows'.")

# Run the function to start the interactive program
decide_campsite()


