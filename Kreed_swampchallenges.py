import time

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
    Prompts the user for a campsite choice and provides a recommendation.
    """
    print("Where would you like to set up camp?")
    print("Options: 'tree', 'ground', or 'willows'")

    # Get user input
    user_choice = input("Enter your choice here: ").lower().strip()

    # Evaluate the user's choice using if/elif/else
    if user_choice == "tree":
        print("\nDecision: Making camp under a tree.")
        print("As you set up camp, a branch snaps and hits you!")
        print("You have lost 10 health")
    elif user_choice == "ground":
        print("\nDecision: Making camp on the ground.")
        print("You sleep on the ground and you sleep peacefully during the night.")
        print("You have lost 0 health")
    elif user_choice == "willows":
        print("\nDecision: Making camp under the willows.")
        print("You sleep underneath the willows and a bird attacks you!")
        print("You have lost 10 health.")
    else:
        # Handles any input that doesn't match the valid options
        print(f"\n'{user_choice}' is not a valid option.")
        print("Please restart the program and choose either 'tree', 'ground', or 'willows'.")

# Run the function to start the interactive program
decide_campsite()
