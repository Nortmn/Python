prof = int(input('Выручка :'))
costs = int(input('Издержки :'))
if prof > costs:
    print(f'Фирма отработала с приблью, рентабельность : {(prof - costs)/prof:0.3252f}')
    employees = int(input('Введите количество работников :'))
    print(f'Доход на одного работника : {(prof - costs)/employees}')
elif prof == costs:
    print('Фирма отработала в ноль')
else:
    print('Фирма отработала с убытком')
