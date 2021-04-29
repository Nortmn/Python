

with open('3_1.txt', encoding='utf-8') as m_f:
    empl = {line.split()[0]: float(line.split()[1]) for line in m_f}
    print(f'Средня з/п = {round(sum(empl.values()) / len(empl), 3)}\n'
          f'С з/п ниже 20000 {[i[0] for i in empl.items() if i[1] < 20000]}')
