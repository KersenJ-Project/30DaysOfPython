print("Somme de tous les nombres de 0 à 100")
sum = 0
for i in range(101):
    sum = sum + i

print(f"The sum of all numbers is {sum}.")

print("Somme de tous les nombres pairs de 0 à 100")
sumEven = 0
for i in range(101):
    if (i % 2 == 0):
        sumEven = sumEven + i


print("Somme de tous les nombres impairs de 0 à 100")
sumOdds = 0
for i in range(101):
    if (i % 2 != 0):
        sumOdds = sumOdds + i

print(f"The sum of all evens is {sumEven}. And the sum of all odds is {sumOdds}.")