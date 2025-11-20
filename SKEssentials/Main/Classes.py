from SKEssentials import SKMath

def display_ETime(t = 0, dp = None, sf = None):
    assert type(t) in (int, float), "Argument <t> must be a real number."
    assert dp is None or (dp >= 0 and sf is None), \
        "Argument <dp> must be a non-negative integer, and arguments <dp> and <sf> are mutually exclusive."
    assert sf is None or (sf >= 0 and dp is None), \
        "Argument <sf> must be a non-negative integer, and arguments <dp> and <sf> are mutually exclusive."

    abs_t = abs(t)
    units = (
        ("ns", 1e-9),
        ("μs", 1e-6),
        ("ms", 0.001),
        ("s", 1),
        ("m", 60),
        ("h", 3_600),
        ("day", 86_400),
        ("year", 31_556_952),
    )

    for i, e in enumerate(units):
        try:
            if e[1] <= abs_t < units[i + 1][1]:
                result = f"{SKMath.short(t / e[1], dp = dp, sf = sf)} {e[0]}"
                if e[0] in ("day", "year") and t / e[1] == 1: result += "s"
                return result
            elif i == 0:
                if 1e-12 <= abs_t < 1e-6:
                    return f"{SKMath.round(t * 1e+9, dp = dp, sf = sf)} ns"
                elif abs_t < 1e-12:
                    return f"{SKMath.round(t, dp = dp, sf = sf)} s"
        except IndexError:
            return f"{SKMath.short(t / e[1], dp = dp, sf = sf)} {e[0]}"