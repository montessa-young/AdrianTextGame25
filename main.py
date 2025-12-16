import time
import random
# This is the file that you will run to play your game
# Import all of the separate functions at the top of this file
# This file should only be function calls.
from Braysen_base_for_encounters import snowy_encounter

from Kreed_swampchallenges import print_slow, decide_campsite, grass_attack
from Kaden_encounter_2 import chance_encounter
from Kyle_challengeskingdomriver import print_slow, backstory, hyper_simple_river_crossing
from encounter_1_B import kingdom_encounter
from Landon_snowy import print_slow, enter_snow, chance_encounter, rebel_encounter, handle_danger, wizard_encounter
from Kyle_Ending import run_qte
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()
backstory()
kingdom_encounter()
kingdom_encounter()
hyper_simple_river_crossing()
chance_encounter()
#decide_campsite()
chance_encounter()
grass_attack()
snowy_encounter()
wizard_encunter()
snowy_encounter()
run_qte()
