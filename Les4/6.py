from itertools import count
from itertools import cycle

m_count = count(10)
m_cycle = cycle('Hello')

for _ in range(6):
    print(f"m_count : {next(m_count)} m_cycle : {next(m_cycle)}")
