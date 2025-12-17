
# This is the file that you will run to play your game
# Import all of the separate functions at the top of this file
# This file should only be function calls.
from Braysen_base_for_encounters import snowy_encounter
from Kreed_swampchallenges import decide_campsite, grass_attack
from Kaden_encounter_2 import swamp_encounter
from encounter_1_B import bandits, wolf
from Landon_snowy import rebel_encounter, handle_danger, wizard_encounter
from Kyle_challengeskingdomriver import backstory, hyper_simple_river_crossing
from Kyle_Ending import ending, run_qte


# Player inventory for the trade system
player_inventory = {
    "gold": 1000,
    "herbs": 0,
    "arrows": 0
}
words_to_type = ["quick", "escape", "action", "now"]
enemy = "dragon"

# Beginning of story
backstory()
# Campsite and River
decide_campsite()
hyper_simple_river_crossing()
# Bandits and wolf encounters
bandits()
wolf()
rebel_encounter()
# Swamp/Fishing Village (Kaden's stuff)
swamp_encounter()
swamp_encounter()
grass_attack()
handle_danger(enemy)
# Snowy Encounters
snowy_encounter()
snowy_encounter()
# Seems like the end..
wizard_encounter()
ending()
run_qte()




