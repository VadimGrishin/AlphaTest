# Системное
yellow = '\x1b[1;93m'
color_end =  '\x1b[0m'

# Ввод базовых переменных
while True:
    hero_name = input("Введите имя вашего персонажа: ").capitalize()
    if hero_name.strip() != '':
        break

while True:
    hero_class = input('Выберите класс вашего персонажа: Человек, Маг, Орк, Эльф: ').lower()
    if hero_class == 'человек' or hero_class == 'маг' or hero_class == 'орк' or hero_class == 'эльф':
        break
    else:
        print('Ошибка. Попробуйте снова')

# Параметры героя
hero_hp = 100
hero_armor = 50
hero_damage = 23

# Стандартные фразы
WELCOME = f"Здравствуй, {hero_class} {yellow}{hero_name}{color_end}!\n" \
    f"Меня зовут {yellow}Дэкой{color_end}. Даже не знаю как ты тут оказался, но мы тебе рады. Я расскажу тебе о наших краях."
stats = f'|{"Имя":^9}|{"Броня":>7}|{"Урон":>6}|{"Здоровье":>10}|\n|{yellow}{hero_name:^9}{color_end}|' \
    f'{yellow}{hero_armor:>7}{color_end}|{yellow}{hero_damage:>6}{color_end}|{yellow}{hero_hp:>10}{color_end}|'
LORE = '''Ты попали в Вальтсардию. 
Это маленькое королевство людей с богатой историей. 
В нем есть 2 крупных города Верхейм и Рейнварден. 
Добро пожаловать!
'''
INTRO = f'Я вижу, что ты боец. Предлагаю тебе устроить спарринг с моим другом {yellow}Фриском{color_end}'
MENU = '''
|------------------------------------------------|
|                     Меню                       |
|------------------------------------------------|
|         Старт / Start - Начать игру            |
|- - - - - - - - - - - - - - - - - - - - - - - - |
|Статистика / Stats - Статистика вашего персонажа|
|- - - - - - - - - - - - - - - - - - - - - - - - |
|      Выход / Exit / Quit - Выход из игры       |
|------------------------------------------------|
'''
exit = 'Увидимся позже! Возвращайся скорее.'

# Вступление
print(WELCOME)
print(LORE)
print(MENU)

# Базовый цикл
while True:
    action = input('Вы в главном меню: ')
    if action.lower() == 'выход' or action.lower() == 'exit' or action.lower() == 'quit':
        print(exit)
        break
    elif action.lower() == 'помошь' or action.lower() == 'help':
        print(MENU)
    elif action.lower() == 'статистика' or action.lower() == 'stats':
        print(stats)
    elif action.lower() == 'старт' or action.lower() == 'start':
        print(INTRO)
        agree =  input('Enter - Да / Другая клавиша - Нет: ')
        if agree == '':
            print('Введи параметры соперника')
            enemy_hp = int(input('Здоровье: '))
            if enemy_hp < hero_damage * 4:
                hero_damage = enemy_hp / 4
            while enemy_hp > 0:
                agree = input('Нанести удар? Enter - Да / Другая клавиша - Нет: ')
                if agree == '':
                    enemy_hp -= hero_damage
                else:
                    print('Вы прервали бой.')
                    break
                if enemy_hp > 0:
                    print(f'Великолепный удар: Здоровье врага - {yellow}{enemy_hp}{color_end}, '
                          f'Ваше здоровье - {yellow}{hero_hp}{color_end}')
            if enemy_hp <= 0:
                print(f'Отличный бой, {yellow}{hero_name}{color_end}. Ты победил!')
    else:
        print(f'Неизвестная команда. Ознакомиться с списоком возможных команд можно введя {yellow}Help{color_end}')