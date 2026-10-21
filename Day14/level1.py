
# Niveau 1

# 1. Différence entre map, filter et reduce

# Map : Applique une fonction à chaque élément d'un itérable.
# Filter : Sélectionne les éléments qui satisfont une condition.
# Reduce : Combine les éléments pour obtenir une seule valeur.


# 2. Différence entre fonction d'ordre supérieur, fermeture et décorateur

# Fonction d'ordre supérieur : Une fonction qui reçoit une autre fonction en paramètre ou qui retourne une fonction.
# Fermeture : Une fonction interne qui conserve l'accès aux variables de la fonction externe.
# Décorateur : Une fonction qui ajoute un comportement à une autre fonction sans modifier son code original.


# 3. Définir des fonctions avant de les utiliser avec map, filter et reduce

from functools import reduce

def carre(nombre):
    return nombre ** 2

def est_pair(nombre):
    return nombre % 2 == 0

def additionner(a, b):
    return a + b


nombres_a_mettre_au_carre = [1, 2, 3, 4, 5]
nombres_carres = map(carre, nombres_a_mettre_au_carre)
print(list(nombres_carres))

nombres_a_filtrer = [1, 2, 3, 4, 5, 6]
nombres_pairs = filter(est_pair, nombres_a_filtrer)
print(list(nombres_pairs))

nombres_a_additionner = [1, 2, 3, 4, 5]
total = reduce(additionner, nombres_a_additionner)
print(total)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 4. Afficher chaque pays avec une boucle for

for country in countries:
    print(country)


# 5. Afficher chaque nom avec une boucle for

for name in names:
    print(name)


# 6. Afficher chaque nombre avec une boucle for

for number in numbers:
    print(number)
