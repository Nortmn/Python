with open('2_1.txt', encoding='utf-8') as m_f:
    n_str = 0
    for m_str in m_f:
        n_str += 1
        n_wrd = 0
        for el in m_str.split():
            n_wrd += 1
        print(f"Слов в {n_str} строке : {n_wrd}")
    print('Всего строк :', n_str)
