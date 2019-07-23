# Програма полностью работает без {yellow}, {color_end}
# Если вместо цвета у вас выводится набор символов, поменяйть строки 7 и 8 на
# yellow = '' и color_end = ''

# Системное (Работает только в PyCharm)

yellow = '\x1b[1;93m'
color_end = '\x1b[0m'

# Види сущностей

hero = {}

roles = {
    'human': {'role_name': 'человек', 'hp': 800, 'max_hp': 800, 'armor': 100, 'damage': 120, 'stamina': 10},
    'mag': {'role_name': 'маг', 'hp': 460, 'max_hp': 600, 'armor': 70, 'damage': 150, 'stamina': 10},
    'ork': {'role_name': 'орк', 'hp': 900, 'max_hp': 900, 'armor': 105, 'damage': 110, 'stamina': 10},
    'elf': {'role_name': 'эльф', 'hp': 700, 'max_hp': 700, 'armor': 80, 'damage': 130, 'stamina': 10},
}

enemies = [
    {'enemy_name': 'Сrimson Bloodhunter', 'hp': 300, 'armor': 20, 'damage': 80},
    {'enemy_name': 'Heaven Vampire', 'hp': 300, 'armor': 40, 'damage': 90},
    {'enemy_name': 'Magical Wolf', 'hp': 300, 'armor': 60, 'damage': 100},
    {'enemy_name': 'Ferocious Tiger', 'hp': 300, 'armor': 80, 'damage': 110},
    {'enemy_name': 'Risen Guard', 'hp': 300, 'armor': 100, 'damage': 120},
]

move_rules = {
    'default': {'damage_koef': 1, 'armor_koef': 1},
    'attack': {'damage_koef': 1.3, 'armor_koef': 0.75},
    'defence': {'damage_koef': 0.75, 'armor_koef': 1.3},
}

chest = [
    'восстановить здоровье полностью',
    'увеличить максимальное здоровье',
    'увеличить урон',
    'увеличить броню',
]

commands = ('Start','Stats', 'Help', 'Exit')

commands_desc = ('Помощь', 'Статистика', 'Начать задание', 'Выход')

instructor = {
    'hp': 1000,
    'armor': 100,
}

# Ввод базовых переменных

while True:
    hero['name'] = input("Введите имя вашего персонажа: \n").capitalize()
    if hero['name'].strip() != '':
        break
print()
artifact = False

#Сундук

def do_chest():
    print(f'Вам открылся сундук "Великих". Выберите награду.')

    s = ''
    for j in range(len(chest)):
        s += f'{j + 1} - {chest[j]}\n'

    if s == '':
        print('Сундук пуст.\n')

    else:
        while True:
            j = input(s + f'{len(chest) + 1} - Оставить всё как есть.')
            if j.isdigit():
                if int(j) - 1 < len(chest) + 1:
                    j = int(j)
                    break
            print(f'Введите значение от 1 до {len(chest) + 1}.')

        if j - 1 < len(chest):
            if chest[j - 1] == 'восстановить здоровье полностью':
                hero['hp'] = hero['max_hp']
            elif chest[j - 1] == 'увеличить максимальное здоровье':
                hero['max_hp'] *= 1.15
            elif chest[j - 1] == 'увеличить урон':
                hero['damage'] *= 1.1
            elif chest[j - 1] == 'увеличить броню':
                hero['armor'] *= 1.2
            chest.pop(j - 1)


while True:
    hero_class = input('Выберите роль вашего персонажа: Человек, Маг, Орк, Эльф: \n').lower()
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
print()
train_damage = hero['damage']

# Стандартные фразы

WELCOME = f"Здравствуй, {hero_class} {yellow}{hero['name']}{color_end}!\n" \
    f"Меня зовут {yellow}Дэкой{color_end}. " \
    f"Даже не знаю как ты тут оказался, но мы тебе рады. Я расскажу тебе о наших краях. "

error_text = f'Неизвестная команда. Ознакомиться с списоком возможных команд можно введя {yellow}Help{color_end}'

stats = \
    f'|{"Имя":^9}|{"Броня":>7}|{"Урон":>6}|{"Здоровье":>10}|\n|{yellow}{hero["name"]:^9}{color_end}|' \
    f'{yellow}{hero["armor"]:>7}{color_end}|{yellow}{hero["damage"]:>6}{color_end}|{yellow}{hero["hp"]:>10}{color_end}|'
LORE = '''Ты попали в Вальтсардию. 
Это маленькое королевство людей с богатой историей. 
В нем есть 2 крупных города Верхейм и Рейнварден. 
Добро пожаловать!
'''

INTRO = f'Я вижу, что ты боец. Предлагаю тебе устроить спарринг с моим другом {yellow}Фриском{color_end}'

MENU = \
    '|' + '- ' * 25 + '|\n'\
    f'|{"Меню":^50}|\n'\
    '|' + '- ' * 25 + '|\n'
for i in range(len(commands)):
    menu_string = f'{commands[i]} - {commands_desc[i]}'
    MENU += \
        f'|{menu_string:^50}|\n'\
        '|' + '- ' * 25 + '|\n'


game_exit = 'Увидимся позже! Возвращайся скорее.'

# Вступление
print(WELCOME)
print(LORE)
print(MENU)

# Базовый цикл
while hero['hp'] > 0 and not artifact:
    action = input('Вы в главном меню: ')
    if action.capitalize() not in commands:
        print(error_text)
    if action.lower() == 'выход' or action.lower() == 'exit' or action.lower() == 'quit':
        print(game_exit)
        break
    elif action.lower() == 'помошь' or action.lower() == 'help':
        print(MENU)
    elif action.lower() == 'статистика' or action.lower() == 'stats':
        print(stats)
    elif action.lower() == 'старт' or action.lower() == 'start':
        print('Приет это снова я - Дэкой. Ну что готов к своему первому заданию? Видишь этот склеп на вершине холма?')
        print('В него уже на заходили 23 года. Говорят там завелось много чудовищь.')
        print(f'Это задание должно быть легким для тебя, еще и мешок золота от {yellow}Гревиаса{color_end} получишь!')
        print(f'{hero["name"]} заходит в склеп и видит несколько комнат. Из каждой доносятся устрашающие звуки.')
        print('Вы решили осматривать каждую комнату по порядку.')

        i = 1
        for enemy in enemies:
            print(f'Вы заходите в {yellow}{i}{color_end} комнату и видите в темном углу страшное существо:\n')
            print(f'|{"Имя":^20}| {"Здорорье":^15}| {"Урон":^15}| {"Броня":^15}|')
            print(f"|{enemy['enemy_name']:^20}| {enemy['hp']:^15}| {enemy['damage']:^15}| {enemy['armor']:^15}|\n")
            is_break = False

            while enemy['hp'] > 0 and hero['hp'] > 0:
                agree = input(f'Выберите вариант хода?\n'
                    f' 1 - Стандарт,\n'
                    f' 2 - Атака ({move_rules["attack"]["damage_koef"]}x урон и {move_rules["attack"]["armor_koef"]}x броня),\n'
                    f' 3 - Защита ({move_rules["defence"]["damage_koef"]}x урон и {move_rules["defence"]["armor_koef"]}x броня),\n'
                    f' Другая клавиша - прервать бой \n')

                if agree == '1':
                    x = 'default'
                elif agree == '2':
                    x = 'attack'
                elif agree == '3':
                    x = 'defence'
                else:
                    print('Вы прервали бой.')
                    is_break = True
                    break

                if hero['damage'] * move_rules[x]["damage_koef"] >= enemy['armor']:
                    enemy['hp'] -= hero['damage'] * move_rules[x]["damage_koef"] - enemy['armor']
                    if enemy['hp'] <= 0:
                        break
                if enemy['damage'] * move_rules[x]["damage_koef"] >= hero['armor']:
                    hero['hp'] -= enemy['damage'] - hero['armor'] * move_rules[x]["armor_koef"]

                if enemy['hp'] > 0:
                    print(f'Великолепный удар: Здоровье врага - {yellow}{enemy["hp"]}{color_end}, '
                          f'Ваше здоровье - {yellow}{hero["hp"]}{color_end}')

            if is_break:
                break

            i += 1

            if hero['hp'] <= 0:
                print(f'Враг оказался сильнее, {yellow}{hero["name"]}{color_end}.')
                break

            if enemy['hp'] <= 0:
                print(f'Отличный бой, {yellow}{hero["name"]}{color_end}. Ты победил!\n')

        artifact = (hero['hp'] > 0) and not(is_break)

if hero['hp'] <= 0:
    print('Вы проиграли.')

elif artifact:
    print('Вы получили артефакт "Великих". Теперь вы обладаете невероятной силой.\n'
          'Используйте её на восстановление справедливости!')
else:
    print('Вы прервали игру\n')
