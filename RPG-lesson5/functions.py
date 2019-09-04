from constants import *
from random import sample, shuffle, randint, uniform
import itertools
import os


def qube6():
    return randint(1, 6)


def qube20():
    return randint(1, 20)


def history():
    say('LORE')


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


def objs_gen():

    n_obj = len(enemies) + N_CHEST_ON_MAP + 1

    obj_places = sorted(sample(range(1, M * N - 1), n_obj))

    objs = list(range(n_obj))
    shuffle(objs)

    yield [(0, 0), '@']

    i, j, = 1, 0
    map_len = M * N

    while i < map_len:

        if j < n_obj and i == obj_places[j]:

            if objs[j] < len(enemies):
                x = str(objs[j])
            else:
                x = '$'
                if objs[j] == n_obj - 1:
                    x = 'A'

            yield ((i // N, i % N), x)
            j += 1

        i += 1


def clear_fog(p_cur):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if p_cur[0] + i in range(M) and p_cur[1] + j in range(N):
                fog[p_cur[0] + i][p_cur[1] + j] = ''


def small_chest(n):

    all_gifts = list(itertools.combinations(chest, n))

    return sample(all_gifts, 1)[0]


def map_redraw(objs_on_map):
    print('\n' * 10)
    for i in range(M):

        s = ''
        for j in range(N):
            x = objs_on_map.get((i, j))

            if x:
                if x == 'A' and not hero['found_arti']:
                    #  скрываем артефакт, пока он не найден
                    x = '$'

            else:
                x = '_'

            if fog[i][j]:
                x = '~'

            s += x + ' '

        print(s)

    stats(hero)


def move(p_cur, objs_on_map):
    def step_fwd():
        nonlocal p_cur, p_next, objs_on_map
        objs_on_map.pop(p_cur)
        p_cur = p_next
        if not hero['found_arti']:
            #  герой "вытесняет" любой объект кроме артефакта
            objs_on_map[p_cur] = '@'

    print('  w  ')
    print('a   d  - движения по карте')
    print('  s  ')
    mv = input()

    if mv == 'a':
        p_next = (p_cur[0], p_cur[1] - 1)
    elif mv == 'd':
        p_next = (p_cur[0], p_cur[1] + 1)
    elif mv == 'w':
        p_next = (p_cur[0] - 1, p_cur[1])
    elif mv == 's':
        p_next = (p_cur[0] + 1, p_cur[1])
    else:
        p_next = p_cur

    obj = objs_on_map.get(p_next)

    if obj:
        if obj == '$':
            iter_chest(hero, chest)
            step_fwd()
        elif obj == 'A':
            # ... Победа
            hero['found_arti'] = True
            step_fwd()

        elif obj.isdigit():
            print(hero)
            print(enemies[int(obj)])
            enemies[int(obj)]['hp'] = enemies[int(obj)]['default_hp']
            hero['breaks_game'] = fight(hero, enemies[int(obj)])

            if hero['breaks_game']:
                return p_cur
            if is_alive(hero):
                step_fwd()
    else:
        if p_next[0] in range(M) and p_next[1] in range(N):
            step_fwd()

    return p_cur


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
        input()


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

