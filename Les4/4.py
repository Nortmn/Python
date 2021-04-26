from random import randint

m_list = [randint(0, 10) for _ in range(0, 15)]
new_list = [i for i in m_list if m_list.count(i) == 1]
print(f"Начальный список : {m_list} \nСписок без повторений : {new_list}")
