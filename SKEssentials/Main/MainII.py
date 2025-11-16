def is_iterable(obj):
    try:
        list(obj)
        return True
    except TypeError:
        return False

def is_list_or_tuple(obj):
    if type(obj) in (str, set, dict):
        return False
    else:
        try:
            list(obj)
            return True
        except TypeError:
            return False