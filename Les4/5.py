from functools import reduce

m_list = [el for el in range(100, 1001, 2)]
print(f"Список: {m_list}\nРезультат: {reduce((lambda x, y: x * y),  [el for el in range(100, 1001, 2)])}")
