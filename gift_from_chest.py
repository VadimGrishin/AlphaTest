import itertools
from random import sample, randint


def small_chest(n):
    chest = list(range(4))

    all_gifts = list(itertools.combinations(chest,n))

    return sample(all_gifts, 1)[0]


for i in range(20):
    n = round(randint(0, 20)/7 + 0.45) # спец функция
    #  n            0     1     2     3
    #  вероятность  0.05  0.35  0.35  0.25
    
    print(small_chest(n))
