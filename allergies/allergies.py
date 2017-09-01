from math import log, floor

class Allergies(object):

    complete_allergies = {
        1 :'eggs', 
        2 : 'peanuts',
        4 : 'shellfish',
        8 : 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128:'cats'
    }

    def __init__(self, number):
        self._number = number

    def is_allergic_to(self, string):
        return string in self.lst

    @property
    def lst(self):
        '''
        dynamically generate list of allergies based on self._number and complete_allergies
        '''
        lst = []
        num = self._number
        while num > 0:
            curr_key = 2 ** floor(log(num,2))
            if curr_key <= 128:
                lst.append(self.complete_allergies[curr_key])
            num -= curr_key

        return lst
