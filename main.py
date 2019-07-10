Name = input("Введите имя вашего персонажа: ")
WelcomeLetter = f"Здравствуй, {Name}!\nМеня зовут Дэкой. Даже не знаю как ты тут оказался, но мы тебе рады. Я расскажу тебе о наших краях."
HP = 100
Armor = 50
Dmg = 23
Stats = f'|   Имя   | Броня | Урон | Здоровье |\n|{Name:^9}|{Armor:>7}|{Dmg:>6}|{HP:>10}|'
Lore = '''Ты попали в Вальтсардию. 
Это маленькое королевство людей с богатой историей. 
В нем есть 2 крупных города Верхейм и Рейнварден. 
Добро пожаловать!
'''
introduction = 'Я вижу, что ты боец. Предлагаю тебе устроить спарринг с моим другом Фриском'
menu = '''
Меню

Старт - Начать игру
Статистика - Статистика вашего персонажа
Выход - Выход из игры

'''
exit = 'Увидимся позже! Возвращайся скорее.'
print(WelcomeLetter)
print(Lore)
print(menu)

while True:
    action = input('Вы в главном меню: ')
    if action == 'выход' or action == "Выход":
        print(exit)
        break
    elif action == 'train' or action == 'Train':
        print('WIP')
    elif action == 'статистика' or action == "Статистика":
        print(Stats)
    elif action == 'старт' or action == 'Старт':
        print(introduction)
        agree =  input('Да / Нет: ')
        if agree == 'Да':
            print('Введи параметры соперника')
            enemyHP = int(input('HP: '))
            if enemyHP < Dmg * 4:
                Dmg = enemyHP / 4
            while enemyHP > 0:
                enemyHP -= Dmg
                agree = input('Нанести удар? Да / Нет: ')
                if agree == 'Да' or agree == 'да':
                    pass
                else:
                    break
                if enemyHP > 0:
                    print(f'Великолепный удар: Здоровье врага - {enemyHP}, '
                          f'Ваше здоровье - {HP}')
            if enemyHP <= 0:
                print(f'Отличный бой, {Name}. Ты победил!')
    else:
        print('Неизвестная команда. Ознакомиться с списоком возможных команд можно введя Help')

