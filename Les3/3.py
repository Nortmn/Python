def m_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


a1 = int(input('Введите первый аргумент :'))
a2 = int(input('Введите второй аргумент :'))
a3 = int(input('Введите третий аргумент :'))
print(f'Сумма равна : {m_func(a1, a2, a3)}')
