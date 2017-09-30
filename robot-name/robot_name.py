"""
This module is for Exercism's 'Robot Names' problem.
To test this module: python robot_name_test.py
"""
import string
import random

class Robot(object):
    '''builds a robot and manages its name'''
    def __init__(self):
        ''' assigns a name for this robot
            for the first time .         '''
        self.reset()

    @staticmethod
    def generate_name():
        '''generates a valid robot name'''
        random.seed()
        return ''.join([string.ascii_uppercase[random.randint(0, 25)] for i in range(2)]) + \
                ''.join([str(random.randint(0, 9)) for i in range(3)])

    def reset(self):
        '''assigns a new name for this robot'''
        self._name = Robot.generate_name()

    @property
    def name(self):
        return self._name
