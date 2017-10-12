def saddle_points(matrix):
    '''
    if matrix is empty, return empty set.
    if matrix rows not equal length, raise a ValueError.

    find the max value for each row,
    then check if it is the min value for its column.
    if so, add coords to saddle_point_set.
    '''
    if not matrix:
        return set()
    if map(len, matrix) != [len(matrix[0])] * len(matrix):
        raise ValueError("Matrix row lengths not equal.")
    saddle_point_set = set()
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == max(row) and val == min(row[j] for row in matrix):
                saddle_point_set.add((i, j))
    return saddle_point_set
