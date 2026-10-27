"""
IndexError
Cause : l'index demandé n'existe pas dans la liste.
"""

numbers = [1, 2, 3, 4, 5]

# Exemple fautif :
# print(numbers[5])

# Correction : les index commencent à 0, donc le dernier index est 4.
print(numbers[4])
