import random
import sys
import time

def print_slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def enter_snow():
    print_slow("After making it through the night the Noble Knight continued onward")
    print_slow("Eventually the Noble Knight makes it into a snowy mountain region 🏔")
    print_slow("The knight continues forward and encounters: ")
enter_snow()

player_inventory = {
    "gold": 10,
    "herbs": 0,
    "arrows": 0,
    "weapons": ["Knight's Sword"]  # starting sword
}

def chance_encounter():
    encounters = ["friendly rebels", "frost guard", "snow leopard"]
    encounter = random.choice(encounters)

    print_slow(f"\nYou encounter: {encounter.upper()}!")

    if encounter == "friendly rebels":
        rebel_encounter()
    else:
        handle_danger(encounter)


def rebel_encounter():
    """Rebels give the player an upgraded sword."""
    print_slow("A group of friendly rebels calls you over as you pass through the snow.")
    print_slow("They notice your Knight's Sword and decide you deserve an upgrade.")

    upgraded_weapon = "Rebel-Forged Greatsword"
    player_inventory["weapons"].append(upgraded_weapon)

    print_slow(f"The rebels present you with a powerful **{upgraded_weapon}**!")
    print_slow("Its blade shines with craftsmanship far beyond your old sword.")
    print_slow(f"Your current weapons: {player_inventory['weapons']}")
    print_slow("You thank the rebels for their generosity and press onward.")


def handle_danger(enemy):
    """Handles any dangerous encounter (fight/run)."""
    choice = input(f"A {enemy} approaches! Do you want to FIGHT or RUN? ").strip().lower()

    if choice == "fight":
        print_slow(f"You stand your ground against the {enemy}!")
        if random.random() < 0.6:
            print_slow(f"You manage to defeat the {enemy}!")
        else:
            print_slow(f"The fight is overwhelming—you retreat but escape safely.")

    elif choice == "run":
        print_slow(f"You try to escape from the {enemy}!")
        if random.random() < 0.8:
            print_slow("You get away successfully!")
        else:
            print_slow("The chase is rough, but you eventually escape unharmed.")

    else:
        print_slow("Your hesitation gives you just enough time to back away and avoid danger.")


# Run encounter
chance_encounter()
