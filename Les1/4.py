s = int(input('Введите число :'))
max_n = s % 10
while s != 0:
    s = s // 10
    if s % 10 > max_n:
        max_n = s % 10
        continue
    if max_n > 8:
        break
print("Наибольшая цифра :", max_n)
