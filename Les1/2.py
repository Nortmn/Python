sec = int(input('Введите время в секундах: '))
hours = sec // 3600
ost_sec = sec % 3600
minutes = ost_sec // 60
seconds = ost_sec % 60
print(f"Время : {hours:02d}:{minutes:02d}:{seconds:02d}")
