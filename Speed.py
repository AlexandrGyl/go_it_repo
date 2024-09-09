print ("Перевірка дотримання вимог контролю швидкості")
maxSpeed =0
minSpeed = 0
speed=0
maxSpeed=int (input ("Введіть максимально дозволену швидкість: "))
minSpeed=int (input ("Введіть мінімально дозволену швидіксть: "))
while (speed !=1000):
    speed=int (input ("Введіть швикість автомобіля: "))
    if (speed !=1000):
        if (speed>maxSpeed and speed<=minSpeed):
            print ("Водій порушив правила дорожнього руху.")
        elif (speed>maxSpeed):
            print ("Недопустима швидкість")
        elif (speed==0):
            print ("Автомобіль не рухається")
        elif (speed<0):
            print ("Відємної швидкості не існує")
        else:
            print ("Правила не порушено")
print ("THE END")
