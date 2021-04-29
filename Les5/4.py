r_d = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('4_2.txt', "w", encoding='utf-8') as n_f:
    with open('4_1.txt', encoding='utf-8') as m_f:
        n_f.writelines([line.replace(line.split()[0], r_d.get(line.split()[0])) for line in m_f])
