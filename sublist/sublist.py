
SUBLIST, SUPERLIST, EQUAL, UNEQUAL = (1,2,3,4)

def check_lists(listA, listB):
    if listA and not listB:
        return SUPERLIST
    if not listA and listB:
        return SUBLIST

    smaller, larger, return_val = \
            (listA, listB, SUBLIST) if len(listA) < len(listB) else\
            (listB, listA, SUPERLIST) if len(listB) < len(listA) else \
            (listA,listB,EQUAL)

    for i in xrange(len(larger) - len(smaller) + 1):
        if larger[i:i+len(smaller)] == smaller:
            return return_val

    return UNEQUAL
