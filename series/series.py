def slices(string,length):
    if length == 0 or length > len(string):
        raise ValueError

    sequence = [int(x) for x in string]
    series = []
    stop_idx = len(sequence) - length
    for i in range(stop_idx + 1):
        series.append(sequence[i:i + length])

    return series
