print("Itérez de 0 à 10 (boucle for)")
for i in range(11):
    print(i)

print("Itérez de 0 à 10 (boucle while)")
count = 0
while count < 11 :
    print(count)
    count = count + 1

print("Itérez de 10 à 0 (boucle for)")
for i in range(11):
    print(10 - i)

print("Itérez de 10 à 0 (boucle while)")
count = 0
while count < 11 :
    print(10 - count)
    count = count + 1

print("Triangle")
for i in range(7):
    print("#" * (i + 1))

print("Carré")
for i in range(8):
    print("#  " * 8)

print("Table de multiplication")
for i in range(11):
    print(f"{i} x {i} = {i*i}")

print("Liste de tech")
list1 = ['Python', 'Numpy','Pandas','Django', 'Flask']
for element in list1:
    print(element)

print("Nombre pair de 0 à 100")
for i in range(101):
    if (i % 2 == 0):
        print(i)

print("Nombre impair de 0 à 100")
for i in range(101):
    if (i % 2 != 0):
        print(i)