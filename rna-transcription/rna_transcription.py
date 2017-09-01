def to_rna(dna):
    dna_to_rna = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
    transcribed = []
    for n in dna:
        if n not in dna_to_rna:
            return ''
        else:
            transcribed.append(dna_to_rna[n])
    return ''.join(transcribed)
