import re
def translate(phrase):
    pig_latin = []
    for word in phrase.split():
        if re.match(r'^([aeiou]+|yt|xr)[a-z]*',phrase):
            pig_latin.append(word + "ay")
        else:
            pig_latin.append(
                    re.sub(
                        r'^(s*qu|[^aeiou]+)([a-z]*)',
                        r'\g<2>\g<1>ay',
                        word
                    )
            )
    
    return ' '.join(pig_latin)
