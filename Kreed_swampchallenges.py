import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)
    print()

def swampchallenges():
    print_slow("As the sun beings to set you decide to make shelter for the night.")
    print_slow("Do you either, (1) make camp under a tree, (2) make camp on the ground, or (3) make shelter under the willows.")

swampchallenges()
