# Écrivez un script qui demande à l'utilisateur d'entrer la base et la hauteur d'un triangle et calcule l'aire de ce triangle

print("Ceci est un script pour calculer l'aire d'un triangle.")

base = float(input("Entrer la base: "))
hauteur = float(input("Entrer la hauteur: "))

area_triangle = 0.5 * base * hauteur

print("L'aire du triangle est", area_triangle)