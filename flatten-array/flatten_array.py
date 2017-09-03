from collections import Sequence 
def flatten(array):
    flattened = []
    for elem in array:
        if not isinstance(elem,str) and isinstance(elem,Sequence):
            flattened.extend(flatten(elem))
        elif elem is not None:
            flattened.append(elem)

    return flattened

