from string import ascii_uppercase as uc
import random

class Robot(object):
    def __init__(self):
        self.reset()
    
    def reset(self):
        random.seed()
        self.name = '%s%s%d%d%d' % \
                (uc[random.randint(0,25)],uc[random.randint(0,25)],\
                random.randint(0,9),random.randint(0,9), \
                random.randint(0,9))

