from countries import countries

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print("Minimun:", ages[0])
print("Maximum:", ages[-1])

ages.append(ages[0])
ages.append(ages[-1])

ages.sort()

millieu = int(len(ages) / 2)
median = 0

if len(ages) % 2 == 0:
    median = (ages[millieu] + ages[millieu - 1]) / 2
else:
    median = ages[millieu]

print("La médiane est de", median)

total = 0

for age in ages:
    total += age

moyenne = total / len(ages)
print("L'âge moyen est de",moyenne)

etendue = ages[-1] - ages[0]
print("Les âges diffèrent sur une étendue de", etendue,"(de " + str(ages[0]) + " à " + str(ages[-1]) + ")")

absolute1 = abs(ages[0] - moyenne)
print("La différence entre la moyenne et le plus petit résultat est de", absolute1)

absolute2 = abs(ages[-1] - moyenne)
print("La différence entre la moyenne et le plus grand résultat est de", absolute2)

middle_countrie = list()

if len(countries) % 2 == 0:
    middle_countrie.append(countries[int(len(countries) / 2)])
    middle_countrie.append(countries[int(len(countries) / 2) - 1])
else:
    middle_countrie.append(countries[int(len(countries) / 2)])

print("Voici le pays au millieu de la liste de pays:", middle_countrie[0])

first_half = countries[:(countries.index(middle_countrie[0]))]
second_half = countries[(countries.index(middle_countrie[0])):]

print(len(countries))
print(len(first_half))
print(len(second_half))

countries_test = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

scandic_countries = countries_test[3:]
print("Voici la liste des pays scandinaves:",scandic_countries)