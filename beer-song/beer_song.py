VERSE_LINES = [
    "{0} {1} of beer on the wall, {2} {3} of beer.\n",
    "Take {0} down and pass it around, ",
    "Go to the store and buy some more, ",
    "{0} {1} of beer on the wall.\n"
]
def verse(number):
    '''
    construct a verse of the beer song
    at a given number of beers
    '''
    bottles = lambda x: "bottle" if x == "1" else "bottles"
    number_str = "No more" if number == 0 else str(number)
    next_number_str = {0: "99", 1: "no more"}.get(number, str(number-1))
    verse_str = VERSE_LINES[0].format(
        number_str,
        bottles(number_str),
        number_str.lower(),
        bottles(number_str)
    )
    if number == 0:
        verse_str += VERSE_LINES[2]
    else:
        verse_str += VERSE_LINES[1].format("it" if number == 1 else "one")
    verse_str += VERSE_LINES[3].format(next_number_str, bottles(next_number_str))
    return verse_str

def song(number1, number2=0):
    return "".join([verse(n)+"\n" for n in range(number1, (number2 - 1), -1)])
