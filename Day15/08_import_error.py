"""
ImportError
Cause : le module existe, mais le nom demandé ne peut pas en être importé.
"""

# Exemple fautif :
# from math import power

# Correction : la fonction s'appelle pow.
from math import pow
print(pow(2, 3))
