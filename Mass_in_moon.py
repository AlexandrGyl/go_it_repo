name = input ("Введіть свое імя: ")
mass = float (input ("Введіть свою вагу на землі: "))
years = 1
while years<=15:
       mass_on_moon = 0.165 * mass
       mass += 1
       years += 1
       print(f"За {years} років {name} буде важити на Місяці {mass_on_moon:2f} кг")
              