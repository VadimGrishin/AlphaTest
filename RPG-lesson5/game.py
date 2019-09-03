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

train_damage = hero['damage']

# Вступление
say('welcome', **hero)
# print(WELCOME)
history()
menu()

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
        objs_on_map = dict([_ for _ in objs_gen()])

        p_cur = (0, 0)
        print(objs_on_map)
        x = 0
        while True:
            map_redraw(objs_on_map)
            p_cur = move(p_cur, objs_on_map)
            print(p_cur)
            #  print(objs_on_map[p_cur])
            if p_cur == -1 or p_cur == 'A':
                break
        map_redraw(objs_on_map)
        #  print(objs_on_map[p_cur])
        artifact = (p_cur == 'A')
        break

    elif action.lower() == 'старт' \
            or action.lower() == 'start':

        artifact = start(hero, enemies)

if hero['hp'] <= 0:
    print('Вы проиграли.')
elif artifact:
    print(
        'Вы получили артефакт "Великих". '
        'Теперь вы обладаете невероятной силой.\n'
        'Используйте её на восстановление справедливости!')
else:

    print('Вы прервали игру\n')
