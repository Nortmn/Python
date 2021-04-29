with open("1_1.txt", 'w') as m_f:
    while True:
        cont = input("Введите строку : ")
        if not cont:
            break
        m_f.write(f"{cont}\n")

m_f = open("1_1.txt", 'r')
print(m_f.read())
