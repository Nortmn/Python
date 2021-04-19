str1 = input('Введите строку :')
m_list = str1.split(' ')
for i, el in enumerate(m_list, 1):
    print(i, el)
