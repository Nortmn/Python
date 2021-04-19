ans = 'y'
m_list = []
el_n = 0
while ans != 'n':
    m_list.append(input('Введите значение :'))
    ans = input('Ввести ещё ? (y/n)')
for i in range(int(len(m_list)/2)):
    in_val = m_list[el_n]
    m_list[el_n] = m_list[el_n+1]
    m_list[el_n + 1] = in_val
    el_n += 2
print(m_list)
