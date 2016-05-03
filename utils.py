def reduce_with_default(operator, iterable, default):
    if len(iterable) == 0:
        return default
    return reduce(operator, iterable)


def copy_and_add(s, item):
    temp = s.copy()
    temp.add(item)
    return temp
