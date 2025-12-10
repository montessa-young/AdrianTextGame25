


def typing_challenge(context_word):
    """A quick time-based typing challenge used for fight or flight outcomes."""
    # Use a more descriptive list of words for the game
    words_to_type = [context_word, "quick", "escape", "action", "now"]
    TIMEOUT = 3  # seconds (made shorter to be challenging)

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

def handle_danger(enemy):
    """Handles any dangerous encounter (fight/run) using the typing challenge."""

    # Ensure choice input is clean
    choice = input(f"A {enemy} approaches! Do you want to FIGHT or RUN? ").strip().lower()

    if choice == "fight":
        print(f"You stand your ground against the {enemy}!")
        # Run the typing challenge; 'fight' is the primary action word for the challenge
        if typing_challenge(context_word="fight"):
            print(f"\n>>> You manage to defeat the {enemy}! <<<")
            # Potential reward logic could go here
        else:
            print(f"\n>>> The fight is overwhelming—you are forced to retreat but escape safely. <<<")

    elif choice == "run":
        print(f"You try to escape from the {enemy}!")
        # Run the typing challenge; 'run' is the primary action word for the challenge
        if typing_challenge(context_word="run"):
            print(f"\n>>> You get away successfully! <<<")
        else:
            print(f"\n>>> The chase is rough, but you eventually escape unharmed. <<<")

    else:
        print("Your hesitation gives you just enough time to back away and avoid danger.")


