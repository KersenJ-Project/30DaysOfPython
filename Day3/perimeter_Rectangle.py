# Écrivez un script qui demande à l'utilisateur d'entrer le côté a, le côté b et le côté c d'un rectangle. Calculez le périmètre du rectangle

print("Ceci est un script pour calculer le perimetre d'un rectangle.")

a = float(input("Entrer le cote a: "))
b = float(input("Entrer le cote b: "))

perimeter = 2 * (a + b)

print("Le perimetre du rectangle est", perimeter)