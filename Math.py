kord_x = input ("Введіть координату точки X: ")
x = float (kord_x)
kord_y = input ("Введіть координату точки Y: ")
y = float (kord_y)
point = (x, y)
match point:
    case (0, 0):
        print ("Точка в центрі координат")
    case (0, kord_y):
        print (f"Точка лежить на осі Y: y={kord_y}")
    case (kord_x, 0):
        print (f"Точка лежить на осі X: x={kord_x}")
    case (kord_x, kord_y):
        print (f"Точка має координати: X={kord_x, kord_y}")
    case _:
        print ("Це не точка")
