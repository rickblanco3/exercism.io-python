SONG_LINES = [
    "On the {0} day of Christmas my true love gave to me",
    "a Partridge in a Pear Tree.\n", "two Turtle Doves",
    "three French Hens", "four Calling Birds",
    "five Gold Rings", "six Geese-a-Laying",
    "seven Swans-a-Swimming", "eight Maids-a-Milking",
    "nine Ladies Dancing", "ten Lords-a-Leaping",
    "eleven Pipers Piping", "twelve Drummers Drumming"
]
ORDINALS = [
    "first", "second", "third", "fourth",
    "fifth", "sixth", "seventh", "eighth",
    "ninth", "tenth", "eleventh", "twelfth"
]

def verse(number):
    verse_str = SONG_LINES[0].format(ORDINALS[number-1])
    if number == 1:
        return verse_str + ", " + SONG_LINES[1]
    while number > 1:
        verse_str += ", " + SONG_LINES[number]
        number -= 1
    return verse_str + ", and " + SONG_LINES[1]

def verses(start, end):
    return ''.join((verse(i)+"\n" for i in range(start, end+1)))

def sing():
    return verses(1, 12)
