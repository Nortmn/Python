def m_func(var1, var2):
    try:
        return var1 / var2
    except ZeroDivisionError:
        return 'Деление на ноль'


x = int(input('Введите 1 число :'))
y = int(input('Введит 2 число :'))
print(m_func(x, y))
