from sys import argv


def m_func():
    try:
        time, rate, prize = map(float, argv[1:])
        print(f"Зарпалата : {time * rate + prize}")
    except ValueError:
        print("Введите только 3 числа ")


m_func()
