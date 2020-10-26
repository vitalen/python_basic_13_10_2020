def my_reduce(func, param):
    result = param[0]
    for el in param[1:]:
        result = func(result, el)
    return result


def my_range(start, end):
    result = []
    while start < end:
        result.append(start)
        start += 1
    return result
