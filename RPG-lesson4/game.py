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

while True:
    hero_class = \
        input('Выберите роль вашего персонажа: Человек, Маг, Орк, Эльф: \n').lower()
    if hero_class == 'человек':
        hero.update(roles['human'])
    elif hero_class == 'маг':
        hero.update(roles['mag'])
    elif hero_class == 'орк':
        hero.update(roles['ork'])
    elif hero_class == 'эльф':
        hero.update(roles['elf'])
    else:
        print('Ошибка. Попробуйте снова')
        continue
    break

WELCOME = \
    f"Здравствуй, {hero_class} {bright_blue}{hero['name']}{color_end}!\n" \
    f"Меня зовут {bright_blue}Дэкой{color_end}. " \
    "Даже не знаю как ты тут оказался, но мы тебе рады. " \
    "Я расскажу тебе о наших краях. "

print()

train_damage = hero['damage']

# Вступление
print(WELCOME)
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
        map_maker()
        x = 0
        while x < 19:
            map_redraw()
            x = move(x)
            if x == -1:
                break
        map_redraw()
        artifact = (x == 19)
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
