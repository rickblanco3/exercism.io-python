import re
def hey(sentence):
    response = "Whatever."
    if re.search("[A-Z]+",sentence) and not re.search("[a-z]",sentence):
        response = "Whoa, chill out!"
    elif re.search("\?\s*$", sentence):
        response = "Sure."
    elif re.search("^\s*$", sentence):
        response = "Fine. Be that way!"

    return response
