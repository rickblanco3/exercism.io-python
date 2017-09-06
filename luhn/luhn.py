class Luhn(object):
    def __init__(self,string):
        self._string = string


    def is_valid(self):
        if len(self._string) <= 1:
            return False

        tmp = self._string
        tmp = tmp.replace(" ","")
        if not tmp.isdigit():
            return False

        tmp = reversed(map(int,tmp))
        luhn_double = lambda x:x*2 if x<5 else x*2 - 9
        tmp = [luhn_double(x) if i%2 != 0 else x for i,x in enumerate(tmp)]

        return sum(tmp) % 10 == 0


