# Exo 2

your_grade = int(input("Quel est votre note ? "))

if your_grade >= 90:
    print("Vous avez un A.")
elif your_grade >= 80:
    print("Vous avez un B.")
elif your_grade >= 70:
    print("Vous avez un C.")
elif your_grade >= 60:
    print("Vous avez un D.")
else:
    print("Vous avez un F.")
    
month = input("Entrez un mois (ex: Janvier, Février, etc.): ").lower()

if month == "Janvier" or month == "Février" or month == "Décembre" or month == "Decemebre" or month == "Fevrier":
    print("C'est l'hiver.")
elif month == "Mars" or month == "Avril" or month == "Mai":
    print("C'est le printemps.")
elif month == "Juin" or month == "Juillet" or month == "Août":
    print("C'est l'été.")
else:
    print("C'est l'automne.")

fruits = ['banana', 'orange', 'mango', 'lemon']

input_fruit = input("Entrez un fruit: ").lower()

if input_fruit in fruits:
    print(f"{input_fruit} est dans la liste.")
else:
    print(f"{input_fruit} n'est pas dans la liste.")
    fruits.append(input_fruit)