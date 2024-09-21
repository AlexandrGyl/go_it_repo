# Задача на цикл
name= str(input ("Введіть своє імя: "))
my_age =  (input ("Введіть свій вік: "))
age = int (my_age)
if age % 2 == 0:
    n = 0
    while n <= age:
        print (n)
        n += 2
else:
     n = 1
     while n <= age:
        print (n)
        n += 2