import math

def round(number, dp = None, sf = None):
    assert type(number) in (int, float), "Argument <number> must be a real number."
    assert dp is None or (type(dp) == int and sf is None), \
        "Argument <dp> must be an integer, and arguments <dp> and <sf> are mutually exclusive."
    assert sf is None or (type(sf) == int and dp is None), \
        "Argument <sf> must be an integer, and arguments <dp> and <sf> are mutually exclusive."

    if type(dp) == int:
        result = (number * 10 ** dp) // 1 / 10 ** dp
        if result % 1 == 0:
            return math.floor(result + 0.5)
        else: return result
    elif type(sf) == int:
        p = math.floor(math.log10(number))
        dp = sf + p - 1
        result = (number * 10 ** dp) // 1 / 10 ** dp
        if result % 1 == 0:
            return math.floor(result + 0.5)
        else: return result
    else:
        if number % 1 == 0:
            return math.floor(number + 0.5)
        return number

def short(number, dp = None, sf = None):
    assert type(number) in (int, float), "Argument <number> must be a real number."
    assert dp is None or (dp >= 0 and sf is None), \
        "Argument <dp> must be a non-negative integer, and arguments <dp> and <sf> are mutually exclusive."
    assert sf is None or (sf >= 0 and dp is None), \
        "Argument <sf> must be a non-negative integer, and arguments <dp> and <sf> are mutually exclusive."

    abs_number = abs(number)

    _map = {
        1_000_000: "million",
        1e+9 : "billion",
        1e+12 : "trillion",
        1e+15 : "quadrillion",
        1e+18 : "quintillion",
        1e+21 : "sextillion",
        1e+24 : "septillion",
        1e+27 : "octillion",
        1e+30 : "nonillion",
        1e+33 : "decillion",
    }

    divisor = 1
    suffix = ""
    for k, e in _map.items():
        if k <= abs_number < 1_000 * k:
            divisor = k
            suffix = e
            break

    if suffix:
        if (number / divisor) % 1 == 0:
            return f"{round(number // divisor, dp=dp, sf=sf)} {suffix}"
        else: return f"{round(number / divisor, dp = dp, sf = sf)} {suffix}"
    else:
        return round(number, dp = dp, sf = sf)
