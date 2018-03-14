import os
import glob
import random

def sound_player(store):
    ### Given specific sound-file
    # if(  ):
        
    ### Pick up a sound-file on sound_vault/ randomly.
    sound_files = glob.glob('../sounds_valut/*')
    random.seed()
    # note:: randrange(Begin, End)
    random_num = random.randrange(0, len(sound_files)+1)
    pickup_sound = sound_files[random_num]

    # debug:: print(pickup_sound)
    os.system('aplay "' + pickup_sound + '"')
