def repeat(n = 2):
    assert type(n) == int, "Argument <n> must be an integer."

    def decorator(f):
        def wrapper(*args, **kwargs):
            if n <= 0:
                return None
            else:
                for i in range(n - 1):
                    f(*args, **kwargs)
                return f(*args, **kwargs)
        return wrapper
    return decorator

def nest(n = 2):
    assert type(n) == int, "Argument <n> must be an integer."

    def decorator(f):
        def wrapper(*args, **kwargs):
            if n <= 0:
                return None
            else:
                result = f(*args, **kwargs)
                for i in range(n - 1):
                    result = f(result)
                return result[0]
        return wrapper
    return decorator