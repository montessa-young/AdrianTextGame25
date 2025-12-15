import time
import random
import sys

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)
    print()
def game_over():
    """A consistent function to call when the player dies."""
    print_slow("\n--- GAME OVER ---")
    sys.exit()

def swampchallenges():
    print_slow("As the sun begins to set you decide to make shelter for the night.")
    print_slow("Do you either, (tree) make camp under a tree, (ground) make camp on the ground, or (willows) make shelter under the willows.")

swampchallenges()

def decide_campsite():
    """
    Prompts the user for a campsite choice and introduces a chance system for outcomes.
    """
    print_slow("Where would you like to set up camp?")
    print_slow("Options: 'tree', 'ground', or 'willows'")
    print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -")

    # Get user input
    user_choice = input("Enter your choice here: ").lower().strip()

    # Determine outcome based on a 10% chance to die
    chance = random.random() # Generates a number between 0.0 and 1.0

    if chance > 0.10: # 10% chance (0.0 to 0.1)
        print_slow("\n💀 A deadly snake attacks in the night! You have died.")
        game_over()
    elif chance < .10:
        print_slow("You go to sleep...")
        campart = r'''
        ______
       /     /\
      /     /  \
     /_____/----\_    (
    "     "          ).
   _ ___          o (:') o
  (@))_))        o ~/~~\~ o
                  o  o  o")
    '''
        print(campart)
        print_slow("✅You have succesfully surivied the night.")
    else:  # 90% chance (0.1 to 1.0)
        # Evaluate the user's choice using if/elif/else for the 'survive' scenarios
        if user_choice == "tree":
            print_slow("\nDecision: Making camp under a tree.")
        elif user_choice == "ground":
            print_slow("\nDecision: Making camp on the ground.")
            print_slow("🌠 You sleep on the ground and you sleep peacefully during the night.")
        elif user_choice == "willows":
            print_slow("\nDecision: Making camp under the willows.")
            print_slow("🦅 You sleep underneath the willows and a bird attacks you!")
        else:
            # Handles any input that doesn't match the valid options
            print_slow(f"\n'{user_choice}' is not a valid option.")
            print_slow("Please restart the program and choose either 'tree', 'ground', or 'willows'.")

# Run the function to start the interactive program
decide_campsite()

def grass_attack():
    print_slow("You pack up your things and head out on your quest..")
    print_slow("As you walk you notice a grassy meadow up ahead.")
    print_slow("You make your way into the meadow and you find some newly made tracks from a big creature.")
    print_slow("Do you either (run) run away from the area, or do you (draw) draw your sword.")
    user_choice = input("Enter your choice here: ").lower().strip()

    bear_present = random.random() < 0.10

    if user_choice == "run":
        print_slow("\nDecision: Run. You try and run away from the area.")
        if bear_present:
            # If you run and the bear was there
            print_slow("The sound of your heavy footsteps alerts the creature nearby.")
            print_slow("💀 A bloodthirsty bear pops out and chases you down. You have died.")
            game_over()
        else:
            # If you run and the area was clear
            print_slow("You run back the way you came. It seems nothing was there after all.")
            print_slow("You turn around and carefully keep going.")

    elif user_choice == "draw":
        print_slow("\nDecision: Draw. You ready your sword for combat.")
        if bear_present:
            # If you draw and the bear was there
            print_slow("You stand your ground, sword ready.")
            print_slow("💀 A bloodthirsty bear pops out. It attacks before you can react. You have died.")
            game_over()

        else:
            # If you draw and the area was clear
            print_slow("You wait patiently with your sword drawn. Nothing appears.")
            print_slow("You see a snowy forest up ahead... you head in that direction.")

    else:
        # Handles invalid input
        print_slow(f"\n'{user_choice}' is not a valid option.")
        print_slow("You hesitate, confused. You decide to keep going anyway.")


grass_attack()





