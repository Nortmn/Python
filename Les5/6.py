m_dict = {}

with open("6_1.txt", encoding='utf-8') as m_f:
    for line in m_f:
        name, stats = line.split(':')
        n_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        m_dict[name] = n_sum
print(m_dict)