scores = {
        ('A','E','I','O','U','L','N','R','S','T')   : 1,
        ('D','G')                                   : 2,
        ('B','C','M','P')                           : 3,
        ('F','H','V','W','Y')                       : 4,
        'K'                                         : 5,
        ('J','X')                                   : 8,
        ('Q','Z')                                   : 10
    }

def score(phrase):
    return sum(
            [scores[s] for s in scores if char in s][0]
            for char in phrase.upper()
        )
