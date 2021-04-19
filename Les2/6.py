prod = []
dict_chara = {'Название': '', 'Цена': '', 'Количество': '', 'Единицы': ''}
dict_an = {'Название': [], 'Цена': [], 'Количество': [], 'Единицы': []}
num = 0
chara = None
control = None
while True:
    control = input("Для выхода введите 'Q', для продолжения нажмите 'Enter', для вывода аналитики 'A'")
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"=" * 20}')
        for key, value in dict_an.items():
            print(f'{key[:25]:>20}: {value}')
    for f in dict_chara.keys():
        chara = input(f'Input feature "{f}"')
        if f == 'Цена' or f == 'Количество':
            dict_chara[f] = int(chara)
        else:
            dict_chara[f] = chara
        dict_an[f].append(dict_chara[f])
    prod.append((num, dict_chara))
