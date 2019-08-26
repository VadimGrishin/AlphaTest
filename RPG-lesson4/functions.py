from constants import *
from random import sample, shuffle, randint, uniform
import itertools


def qube6():
    return randint(1, 6)


def qube20():
    return randint(1, 20)


def history():
    say('LORE')


def map_gen():
    n_obj = len(enemies) + N_CHEST_ON_MAP
    obj_places = sorted(sample(range(MAP_SIZE - 1), n_obj))

    objs = list(range(n_obj))
    shuffle(objs)

    i, j, = 0, 0

    while i < MAP_SIZE - 1:
        x = '_'
        if j < n_obj and i == obj_places[j]:
            if objs[j] < len(enemies):
                x = str(objs[j])
            else:
                x = '$'

            j += 1

        i += 1
        yield x


def small_chest(n):

    all_gifts = list(itertools.combinations(chest, n))

    return sample(all_gifts, 1)[0]


def pause():
    input('Нажмите Enter')


def train():
    print(INTRO)
    agree = input('Enter - Да / Другая клавиша - Нет: ')

    if agree == '':
        print('Введи параметры соперника')
        instructor['hp'] = int(input('Здоровье: '))
        hero['damage'] = int(input('На сколько ты силён: '))
        print(
            f'Здоровье врага - {instructor["hp"]}\n'
            f'Ваше здоровье - {hero["hp"]}\n')
        if instructor["hp"] < hero['damage'] * 4:
            hero['damage'] = instructor["hp"] / 4

    while instructor["hp"] > 0:
        input('Нанести удар - Enter')
        instructor["hp"] -= hero['damage']
        print('Великолепный удар:\n'
              f'Здоровье врага - {instructor["hp"]}\n'
              f'Ваше здоровье - {hero["hp"]}\n')

    print(f'Отличный бой, {hero["name"]}. Ты победил!')


def is_alive(person):
    if person['hp'] <= 0:
        return False
    else:
        return True


def stats(person):
    statistics = \
        f'|{"Имя":^{len(person["name"]) + 4}}|' \
        f'{"Броня":^7}|' \
        f'{"Урон":^6}|' \
        f'{"Здоровье":^10}|\n' \
        f'|{bright_blue}{person["name"]:^{len(person["name"]) + 4}}{color_end}|' \
        f'{bright_blue}{person["armor"]:^7}{color_end}|' \
        f'{bright_blue}{person["damage"]:^6}{color_end}|' \
        f'{bright_blue}{person["hp"]:^10}{color_end}|'
    print(statistics)
    print()


def menu():
    menu = \
        '|' + '- ' * 25 + '|\n' \
        f'|{yellow}{"Меню":^50}{color_end}|\n' \
        '|' + '- ' * 25 + '|\n'
    for i in range(len(commands)):
        menu_string = f'{bright_blue}{commands[i]}{color_end} - {yellow}{commands_desc[i]}{color_end}'
        menu += \
            f'|{menu_string:^74}|\n' \
            '|' + '- ' * 25 + '|\n'
    print(menu)


def start(h, es):
    print(
        'Привет это снова я - Дэкой. \n'
        'Ну что готов к своему первому заданию? Видишь этот склеп на вершине холма?\n'
        'В него уже не заходили 23 года. \n'
        'Говорят там завелось много чудовищ.\n'
        f'Это задание должно быть легким для тебя, еще и мешок золота от {bright_blue}Гревиаса{color_end} получишь!\n'
        f'{bright_blue}{h["name"]}{color_end} заходит в склеп и видит несколько комнат. '
        'Из каждой доносятся устрашающие звуки.\n'
        'Вы решили осматривать каждую комнату по порядку.'
    )
    fight_break = fight_all(h, es)

    return (is_alive(h)) and not fight_break


def fight_all(h, es):
    i = 1
    fight_break = False
    for e in es:
        e['hp'] = e['default_hp']
        print(f'Вы заходите в {bright_blue}{i}{color_end}-ю комнату и видите в темном углу страшное существо:\n')
        stats(e)
        fight_break = fight(h, e)
        if fight_break:
            break
        i += 1

        if not is_alive(h):
            say('lose', **h)
            break

        if not is_alive(e):
            print(
                f'Отличный бой, {bright_blue}{h["name"]}{color_end}. '
                f'Ты победил!\n')
        do_chest(h, chest)

    return fight_break


def say(text, *args, **kwargs):
    assert text in TEXTS, 'В этом месте может быть ваш текст'
    print(TEXTS[text].format(*args, **kwargs, bright_blue=bright_blue, color_end=color_end), end='')
    return ''


def fight(h, e):
    is_break = False
    while is_alive(e) and is_alive(h):
        agree = choice_view(moves)
        if agree == 0:
            x = 'default'
        elif agree == 1:
            x = 'attack'
        elif agree == 2:
            x = 'defence'
        elif agree == 3:
            print('Вы прервали бой.')
            is_break = True
            for (key, val) in roles.items():
                if val['role_name'] == hero['role_name']:
                    hero.update(roles[key])
            break
        fight_round(h, e, x)
        if not is_alive(e):
            break

    return is_break


def fight_round(h, e, x):
    #  удар героя
    y = qube6()
    hit_hero = h['damage'] * move_rules[x]["damage_kf"] + y - e['armor']

    hit_hero *= critical_kf(qube20())

    if hit_hero > 0:
        e['hp'] -= hit_hero
        if not is_alive(e):
            return

    #  удар врага
    y = qube6()
    hit_enemy = e['damage'] - h['armor'] * move_rules[x]["armor_kf"] + y

    hit_enemy *= critical_kf(qube20())

    if hit_enemy >= 0:
        hero['hp'] -= hit_enemy

    if is_alive(e):
        print(f'Великолепный удар: Здоровье врага - {bright_blue}{e["hp"]}{color_end}, '
              f'Ваше здоровье - {bright_blue}{hero["hp"]}{color_end}')


def critical_kf(t):
    if t in range(19, 21):
        return 3
    elif t in range(1, 3):
        return 0
    return 1


def map_redraw(game_map):
    print(''.join(game_map))


def move(x, game_map):
    input('Ход - Enter')
    if game_map[x + 1] == '_':
        game_map[x] = '_'
        x += 1
        game_map[x] = '@'

    elif game_map[x + 1] == '$':
        iter_chest(hero, chest)
        game_map[x] = '_'
        x += 1
        game_map[x] = '@'

    elif game_map[x + 1].isdigit():
        print(hero)
        print(enemies[int(game_map[x + 1])])
        enemies[int(game_map[x + 1])]['hp'] = enemies[int(game_map[x + 1])]['default_hp']
        k = fight(hero, enemies[int(game_map[x + 1])])
        if is_alive(hero) and not k:
            game_map[x] = '_'
            x += 1
            game_map[x] = '@'
        else:
            x = -1
    return x


def iter_chest(h, ch):

    n = round(randint(0, 20) / 20 * 3 + 0.45)  # спец преобразование:
    #  n            0     1     2     3
    #  вероятность  0.05  0.35  0.35  0.25

    if n:
        small_ch = small_chest(n)

        j = choice_view(small_ch)

        say('selected_treasure', small_ch[j])
        if small_ch[j] == 'восстановить здоровье полностью':
            h['hp'] = h['max_hp']
        elif small_ch[j] == 'увеличить максимальное здоровье':
            h['max_hp'] *= uniform(chest_ranges['max_hp']['min'], chest_ranges['max_hp']['max'])
        elif small_ch[j] == 'увеличить урон':
            h['damage'] *= uniform(chest_ranges['damage']['min'], chest_ranges['damage']['max'])
        elif small_ch[j] == 'увеличить броню':
            h['armor'] *= uniform(chest_ranges['armor']['min'], chest_ranges['armor']['max'])
    else:
        say('empty_chest')


def do_chest(h, ch):
    print(
        'Вам открылся сундук "Великих". '
        'Выберите награду.')

    if len(ch) == 0:
        print('Сундук пуст.\n')

    else:
        j = choice_view(ch)
        if ch[j] != 'оставить на следующий раз':

            if ch[j] == 'восстановить здоровье полностью':
                h['hp'] = h['max_hp']
            elif ch[j] == 'увеличить максимальное здоровье':
                h['max_hp'] *= uniform(chest_ranges['max_hp']['min'], chest_ranges['max_hp']['max'])
            elif ch[j] == 'увеличить урон':
                h['damage'] *= uniform(chest_ranges['damage']['min'], chest_ranges['damage']['max'])
            elif ch[j] == 'увеличить броню':
                h['armor'] *= uniform(chest_ranges['armor']['min'], chest_ranges['armor']['max'])
            ch.pop(j)


def choice_view(menu_list, ask='Выберите'):

    print(ask)
    for i, item in enumerate(menu_list):
        print(f'{i} - {item}')

    while True:
        i = input('')
        if i.isdigit():
            i = int(i)
            if i < len(menu_list):
                return i

