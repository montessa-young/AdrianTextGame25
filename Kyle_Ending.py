import sys
import time
def print_slow(text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")

def print_slow2(text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")

print_slow("You venture on with your magic potion feeling confident that the potion will easily defeat the Frost Kings dragon.🌋")
print_slow("Eventually reach the volcano and you pause for a moment, thinking about the things you've fought, and all the things yet to come..")
print_slow("You swallow your worry and enter the volcano entrance.")
print_slow("As you enter, you suddently are hit with a strong gust of heat instantly causing you to become tired and dizzy.😓")
print_slow("Just then you hear roaring in the distance and you quickly pull your potion.")
print_slow("Quick time event coming soon be prepared❗")
print_slow("Just then, the Frost King and his loyal dragon appears in front of you with a sudden crash.👑💥")

import time
import sys

# --- Game Constants ---
REQUIRED_WORD = "THROW"
TIME_LIMIT = 6.0  # Seconds

# --- Game Setup ---
def run_qte():
    """Runs the Quick Time Event: Dragon's Fury."""

    print("=" * 50)
    print("🐉 DRAGON'S FURY: QUICK TIME EVENT! 🐉")
    print("The ice dragon is charging its deadly blast!")
    print(f"You must type the incantation '{REQUIRED_WORD}' in under {TIME_LIMIT} seconds!")
    print("=" * 50)

    # 1. Record the start time
    start_time = time.time()

    try:
        # 2. Get user input
        # Note: The program waits here until the user presses Enter.
        # The time taken is recorded after this line executes.
        user_input = input("Type the word NOW: ").strip().upper()

        # 3. Record the end time
        end_time = time.time()

        # 4. Calculate the time elapsed
        elapsed_time = end_time - start_time

        # 5. Check the result
        print("-" * 50)
        print(f"Time taken: {elapsed_time:.3f} seconds")

        if elapsed_time <= TIME_LIMIT and user_input == REQUIRED_WORD:
            # --- SUCCESS PATH ---
            print_slow2("\n!!! SUCCESS !!!")
            print_slow2("You quickly threw the potion in time!")
            print_slow2(f"The potion shattered the dragon's ice magic.")
            print_slow2("You lunge an attack, shoving your sword straight into the dragons ice heart.💔")
            print_slow2("You have slain the dragon! 🐲💥")
            print_slow2("-----------------------------------------------------------------------------")

            print_slow("The Frost King, terrified, quickly hops off of his dragon and attempts to run away.😟🏃")
            print_slow("Suddenly, the ground beneath him cracks open, revealing hot lava below.")
            print_slow("He tries to regain his balance but he slips and falls to his firey demise.🔥")
            print_slow2("-----------------------------------------------------------------------------------")
            print_slow("As the volcano shakes, you quickly retreive the Great Dragons egg and return home more cautious than ever before.")
            print_slow("You soon bring the Great Dragons egg to the King and he rewards you with a life time of wealth and respect.")
            print_slow("Aswell as the Kings bravest soldier to ever live...👑")
        elif elapsed_time > TIME_LIMIT:
            # --- FAILURE PATH: TIMEOUT ---
            print("\n!!! FAILURE !!!")
            print("Time ran out! You were too slow!")
            print(f"The dragon's icy breath freezes you instantly. You are defeated. 💀❄️")

        else: # user_input != REQUIRED_WORD
            # --- FAILURE PATH: WRONG WORD ---
            print("\n!!! FAILURE !!!")
            print(f"You typed '{user_input}'. You trip as the rock beneath you shifts and you miss the potion!")
            print(f"The dragon's icy breath freezes you instantly. You are defeated. 💀❄️")

    except EOFError:
        print("\n\nGame cancelled.")
    except KeyboardInterrupt:
        print("\n\nGame stopped.")

# Execute the game function
if __name__ == "__main__":
    run_qte()
