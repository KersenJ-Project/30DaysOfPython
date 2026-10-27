"""
ZeroDivisionError
Cause : une division par zéro est tentée.
"""

# Exemple fautif :
# print(1 / 0)

# Correction : vérifier que le diviseur n'est pas égal à zéro.
diviseur = 2

if diviseur != 0:
    print(1 / diviseur)
else:
    print("Impossible de diviser par zéro.")
