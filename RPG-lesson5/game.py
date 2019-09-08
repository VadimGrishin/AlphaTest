#!/usr/bin/python
# -*- coding: utf-8 -*-

from functions import *
from constants import *

while True:
    hero['name'] = \
        input('Введите имя вашего персонажа: \n').capitalize()
    if hero['name'].strip() != '':
        break
print()

classes = [role for role in roles]
class_names = [role['role_name'] for role in roles.values()]

j = choice_view(class_names, 'Выберите класс персонажа')
hero_class = classes[j]
hero.update(roles[hero_class])

hero['found_arti'] = False
hero['breaks_game'] = False

train_damage = hero['damage']

# Вступление
say('welcome', **hero)
# print(WELCOME)
history()
menu()

objs_on_map = dict([_ for _ in objs_gen()])

p_cur = (0, 0)
clear_fog(p_cur)

# Базовый цикл
while hero['hp'] > 0 and not artifact:
    action = \
        input('Вы в главном меню: \n')
    if action.capitalize() not in commands:
        print(error_text)
    if action.lower() == 'выход' \
            or action.lower() == 'exit':
        print(game_exit)
        break
    elif action.lower() == 'помошь' \
            or action.lower() == 'help':
        menu()
    elif action.lower() == 'статистика' \
            or action.lower() == 'stats':
        stats(hero)
    elif action.lower() == 'train':
        train()
    elif action.lower() == 'map':

        print('Для отладки', objs_on_map)
        x = 0
        while True:
            map_redraw(objs_on_map, hero)
            p_cur = move(p_cur, objs_on_map, hero)
            clear_fog(p_cur)

            if hero['breaks_game'] or hero['found_arti']:
                break
        map_redraw(objs_on_map, hero)

    elif action.lower() == 'save':
        save(objs_on_map, hero)

    elif action.lower() == 'load':
        hero, M, N, objs_on_map = load()
        for k, v in objs_on_map.items():
            if v == '@':
                p_cur = k
                break
        hero['breaks_game'] = False

    elif action.lower() == 'delete':
        delete()

    if hero['hp'] <= 0:

        save_request = input('Вы проиграли\n Сохранить состояние? y/n')

        if save_request == 'y':
            print('сохраняем...')
            #  n = get_last_sv_nmb() + 1

    elif hero['found_arti']:
        print(
            'Вы получили артефакт "Великих". '
            'Теперь вы обладаете невероятной силой.\n'
            'Используйте её на восстановление справедливости!')
        break

    elif hero['breaks_game']:
        save_request = input('Вы прервали игру\n Сохранить состояние? y/n')

        if save_request == 'y':
            print('сохраняем...')
            save(objs_on_map, hero)  #  f'save_objs_{n}.txt'
