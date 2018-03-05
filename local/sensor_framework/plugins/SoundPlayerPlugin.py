import os
import glob
import random

def sound_player():
    ### Pick up a sound-file on sound_vault/ randomly.
    sound_files = glob.glob('../sounds_valut/*')
    random.seed()
    random_num = random.randrange(0, len(sound_files))
    pickup_sound = sound_files[random_num]

    # debug:: print(pickup_sound)
    os.system('aplay "' + pickup_sound + '"')
