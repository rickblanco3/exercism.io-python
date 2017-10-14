from collections import OrderedDict

ACTIONS = OrderedDict([
    (1, "wink"),
    (2, "double blink"),
    (4, "close your eyes"),
    (8, "jump")
])

def handshake(number):
    if number < 1:
        return []
    if isinstance(number, str):
        try:
            number = int(number, 2)
        except ValueError:
            return []
    moves = [ACTIONS[k] for k in filter(lambda x: number & x, ACTIONS)]
    if number > 16:
        moves = moves[::-1]
    return moves

def code(secret_code):
    for move in secret_code:
        if move not in ACTIONS.values():
            return '0'
    number = sum([k for k, v in ACTIONS.items() if v in secret_code])
    if ACTIONS.values().index(secret_code[0]) > ACTIONS.values().index(secret_code[-1]):
        number += 16
    return "{:b}".format(number)
