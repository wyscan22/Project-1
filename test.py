from SKEssentials.Main import Decorators as MDec
from SKEssentials import SKTime

@MDec.repeat()
def print_hi(name = "MPK"):
    print(f"Hi, {name}")

print_hi()