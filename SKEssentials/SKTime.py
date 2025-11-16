from SKEssentials.Main import Classes as MCla
import time

def timed(f):
    def wrapper(*args, **kwargs):
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

        t = time.time()
        result = f(*args, **kwargs)
        display_time = time.time() - t

        for i, e in enumerate(units):
            try:
                if e[1] < display_time < units[i + 1][1]:
                    display_time = f"{str(display_time / e[1])} {e[0]}"
                    break
            except IndexError:
                if e[1] < display_time:
                    display_time = f"{str(display_time / e[1])} {e[0]}"
                else:
                    display_time = f"{str(display_time)} s"

        print(f"{f} took {display_time}")
        return result
    return wrapper