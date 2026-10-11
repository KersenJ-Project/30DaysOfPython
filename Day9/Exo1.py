# Exo 1

your_age = int(input("Quel est votre âge ? "))

if your_age >= 18:
    print("Vous pouvez apprendre a conduire.")
else:
    print(f"Il vous reste {18 - your_age} ans avant de pouvoir apprendre a conduire.")

my_age = 18

if my_age >= your_age:
    print(f"J'ai {my_age - your_age} ans de plus que vous.")
else:
    print(f"Vous avez {your_age - my_age} ans de plus que moi.")

a = int(input("Entrez un nombre: "))
b = int(input("Entrez un autre nombre: "))

if a > b:
    print(f"{a} est plus grand que {b}.")
elif a < b:
    print(f"{a} est plus petit que {b}.")
else:
    print(f"{a} est égal à {b}.")