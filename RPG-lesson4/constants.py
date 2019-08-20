
yellow = '\x1b[1;92m'
dark_blue = '\x1b[1;94m'
pink = '\x1b[1;95m'
bright_blue = '\x1b[1;4;96m'
grey = '\x1b[1;97m'
color_end = '\x1b[0m'

hero = {}

artifact = False

commands = ('Start', 'Stats', 'Help', 'Exit', 'Map')

roles = {
    'human': {
        'role_name': 'человек',
        'hp': 800,
        'max_hp': 800,
        'armor': 100,
        'damage': 120,
        },
    'mag': {
        'role_name': 'маг',
        'hp': 44460,
        'max_hp': 46440,
        'armor': 440,
        'damage': 1520,
        },
    'ork': {
        'role_name': 'орк',
        'hp': 900,
        'max_hp': 900,
        'armor': 105,
        'damage': 110,
        },
    'elf': {
        'role_name': 'эльф',
        'hp': 700,
        'max_hp': 700,
        'armor': 80,
        'damage': 130,
        },
    }

enemies = [{
    'name': 'Crimson Bloodhunter',
    'default_hp': 300,
    'armor': 20,
    'damage': 80,
    }, {
    'name': 'Heaven Vampire',
    'default_hp': 300,
    'armor': 40,
    'damage': 90,
    }, {
    'name': 'Magical Wolf',
    'default_hp': 300,
    'armor': 60,
    'damage': 100,
    }, {
    'name': 'Ferocious Tiger',
    'default_hp': 300,
    'armor': 80,
    'damage': 110,
    }, {
    'name': 'Risen Guard',
    'default_hp': 300,
    'armor': 100,
    'damage': 120,
    }]

move_rules = {'default': {'damage_kf': 1, 'armor_kf': 1},
              'attack': {'damage_kf': 1.3, 'armor_kf': 0.75},
              'defence': {'damage_kf': 0.75, 'armor_kf': 1.3}}

chest_ranges = {
    'max_hp': {
        'min': 2,
        'max': 10,
    },
    'damage': {
        'min': 2,
        'max': 10,
    },
    'armor': {
        'min': 2,
        'max': 10,
    },
}

chest = \
    [
        'восстановить здоровье полностью',
        'увеличить максимальное здоровье',
        'увеличить урон',
        'увеличить броню',
    ]

commands_desc = \
    (
        'Начать задание',
        'Статистика',
        'Помощь',
        'Выход',
        'Пройти коридор испытаний'
     )

instructor = {'hp': 1000, 'armor': 100}

moves = [
    'Стандарт',
    f'Атака ({move_rules["attack"]["damage_kf"]}x урон и {move_rules["attack"]["armor_kf"]}x броня)',
    f'Защита ({move_rules["defence"]["damage_kf"]}x урон и {move_rules["defence"]["armor_kf"]}x броня)',
    'Прервать бой',
]

error_text = \
    'Неизвестная команда. ' \
    f'Ознакомиться с списоком возможных команд можно введя {bright_blue}Help{color_end}'

LORE = f'Ты попали в {bright_blue}Вальтсардию{color_end}. \n' \
       'Это маленькое королевство людей с богатой историей. \n' \
       f'В нем есть 2 крупных города {bright_blue}Верхейм{color_end} и {bright_blue}Рейнварден{color_end}. \n' \
       'Добро пожаловать!\n'

INTRO = \
    'Я вижу, что ты боец. ' \
    f'Предлагаю тебе устроить спарринг с моим другом {bright_blue}Фриском{color_end}'

game_exit = 'Увидимся позже! Возвращайся скорее.'

say_list = {
    'error_text':
        'Неизвестная команда. '
        f'Ознакомиться с списоком возможных команд можно введя {bright_blue}Help{color_end}',

    'LORE':
        f'Ты попали в {bright_blue}Вальтсардию{color_end}. \n'
        'Это маленькое королевство людей с богатой историей. \n'
        f'В нем есть 2 крупных города {bright_blue}Верхейм{color_end} и {bright_blue}Рейнварден{color_end}. \n'
        'Добро пожаловать!\n',

    'INTRO':
        f'Я вижу, что ты боец. Предлагаю тебе устроить спарринг с моим другом {bright_blue}Фриском{color_end}',

    'game_exit':
        'Увидимся позже! Возвращайся скорее.',
}

NAMES = {
    'name': 'Имя',
    'role_name': 'Роль',
    'hp': 'Здоровье',
    'max_hp': 'Максимальное здоровье',
    'damage': 'Урон',
    'armor': 'Броня',
    'stamina': 'Выносливость',
    'hit': 'Нанесено урона за раунд',
    'up_max_hp': 'Увеличить максимальное здоровье',
    'up_damage': 'Увеличить урон',
    'up_armor': 'Увеличить броню',
}

TEXTS = {
    'error_text': 'Неизвестная команда. '
                  'Ознакомиться с списоком возможных команд можно введя {bright_blue}Help{color_end}',

    'LORE': 'Ты попал в {bright_blue}Вальтсардию{color_end}. \n '
            'Это маленькое королевство людей с богатой историей. \n'
            'В нем есть 2 крупных города {bright_blue}Верхейм{color_end} и {bright_blue}Рейнварден{color_end}. \n'
            'Добро пожаловать!\n',

    'INTRO': 'Я вижу, что ты боец. Предлагаю тебе устроить спарринг с моим другом {bright_blue}Фриском{color_end}',

    'game_exit': 'Увидимся позже! Возвращайся скорее.',

    'lose': 'Враг оказался сильнее, {bright_blue}{name}{color_end}. ',
}

game_map = ['_'] * 20
