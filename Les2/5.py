m_list = [7, 5, 3, 3, 2]
ans = 'y'
while ans != 'n':
    n_el = int(input('Введите число :'))
    for i in range(len(m_list)):
        if n_el == m_list[i]:
            m_list.insert(i + 1, n_el)
            break
        elif n_el > m_list[i]:
            m_list.insert(i, n_el)
            break
        elif n_el < m_list[-1]:
            m_list.append(n_el)
            break
    print(m_list)
    ans = input('Продолжить ? (y/n)')
