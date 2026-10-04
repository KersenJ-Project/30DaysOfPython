# 1. Ex de variables

# Nombres
# Entier
a = 10
# Flottant
b = 2.5

# Complexe, j = imaginary values
c = 1 + 2j

# Chaîne de caractères
d = "Hello"

# Booléen
e = False

# Liste
f = ["x", "y", "z"]

# Tuple, liste non modifiable
g = ("a", "b", "c")

# Ensemble, element unique seulement
h = {"apple", "banana", "cherry"}

# Dictionnaire, equivalent de hashmap
i = {"name": "John", "age": 30}

# 2. Euclidean distance (Pythagore), Values:  (2,3) and (10,8)
import math

x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt(((x2 - x1)**2) + ((y2-y1)**2)) # In python we can use ** 0.5 to calculate the square root

print(distance)