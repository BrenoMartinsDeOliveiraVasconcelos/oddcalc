import math

def calc_oddies(tries: int, chance: float):
   return 1 - (1-chance)**tries


def calc_tries(percent: float, chance: float):
    return math.ceil((math.log(1-percent))/(math.log(1-chance)))


if __name__=='__main__':
    print(calc_oddies(tries=50, chance=1/100)*100)
    print(calc_tries(0.395, 1/100))
    