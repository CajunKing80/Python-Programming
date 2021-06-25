
def slices(series, length):
    if length > len(series):
        raise ValueError("Meaningful Error")
    if length <= 0:
        raise ValueError("Meaningful Error")
    string_of_digits = []
    for i in range(len(series) - length + 1):
        string_of_digits.append(series[i:i+length])
    return string_of_digits