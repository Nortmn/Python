x = float(input('numb :'))
y = float(input('step :'))


def f_pow(m_value, m_pow):
    result = 1
    m_pow_abs = abs(m_pow)
    while m_pow_abs > 0:
        if m_pow_abs % 2 == 1:
            result *= m_value
        m_value *= m_value
        m_pow_abs //= 2
    if m_pow < 0:
        return 1 / result
    else:
        return f'Результат : {round(result, 3)}'


print(f_pow(x, y))
