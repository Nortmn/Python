def int_func(str_in):
    for w in str_in.split():
        ch_i = 0
        for ch in w:
            if 97 <= ord(ch) <= 122:
                ch_i += 1
    if ch_i == len(w):
        print(str_in.title())
    else:
        print(f'Ввеите "{w}" только прописными латинскими буквами')
    return


int_func(input('Введите строку латинскими буквами :'))
