from random import randint

m_list = [randint(0, 100) for _ in range(0, 10)]
new_list = [m_list[i] for i in range(1, len(m_list)) if m_list[i] > m_list[i - 1]]
print(m_list)
print(new_list)
