a = [(1, 2, 3), [1, 2, 3], 'abc', 1254, {1, 2, 3}]

def return_dict(data):
    result = {}
    for d in data:
        try:
            result[d] = type(d).__name__
        except TypeError:
            result[str(d)] = type(d).__name__
    return result



print(return_dict(a))


