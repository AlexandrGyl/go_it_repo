# Перевірка в якій області координат розташовано точку
Xkord = input ("Введіть координату Х: ")
x = float (Xkord)
Ykord = input ("ВВедіть координату Y: ")
y = float (Ykord)
if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("Перша чверть")
    else:  # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:  # x < 0, y > 0
        print("Друга чверть")
    else:  # x < 0, y < 0
        print("Третя чверть")


