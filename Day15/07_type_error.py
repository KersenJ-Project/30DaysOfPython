"""
TypeError
Cause : une opération est appliquée à des types incompatibles.
"""

# Exemple fautif :
# print(4 + "3")

# Correction 1 : convertir la chaîne en entier.
print(4 + int("3"))

# Correction 2 (alternative) : convertir le nombre en chaîne.
print(str(4) + "3")
