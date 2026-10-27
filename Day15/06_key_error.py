"""
KeyError
Cause : la clé demandée n'existe pas dans le dictionnaire.
"""

users = {"name": "Asab", "age": 25, "country": "Finland"}

# Exemple fautif :
# print(users["county"])

# Correction :
print(users["country"])

# Variante pratique : get() évite l'erreur si la clé est absente.
print(users.get("city", "Ville inconnue"))
