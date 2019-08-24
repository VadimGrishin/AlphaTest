from random import sample, shuffle

MAP_SIZE = 20

def map_gen():
    obj_places = sorted(sample(range(MAP_SIZE), 9))

    objs = list(range(9))
    shuffle(objs)

    i, j, = 0, 0

    while i < MAP_SIZE:
        x = '_'
        if j < 9 and i == obj_places[j]:
            if objs[j] < 5:
                x = str(objs[j])
            else:
                x = '$'

            j += 1

        i += 1
        yield x
        
game_map = [_ for _ in map_gen()]

print(' '.join(game_map))
