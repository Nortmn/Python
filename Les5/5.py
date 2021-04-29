from random import  randint

with open("5_1.txt", "w", encoding='utf-8') as m_f:
    m_list = [randint(1, 100) for _ in range(100)]
    m_f.write(" ".join(map(str, m_list)))

print("Сумма элементов :", sum(m_list))
