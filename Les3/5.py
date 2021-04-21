def m_func():
    full = 0
    ans = True
    while ans:
        res = 0
        str_in = input('Введите строку чисел:').split()
        for i in range(len(str_in)):
            if str_in[i] == 'q':
                ans = False
                break
            else:
                try:
                    res += int(str_in[i])
                except ValueError:
                    print(f'Чтобы выйти введите "q"')
        full += res
        print('Промежуточный результат :', res)
    print('Конечный результат :', full)


m_func()
