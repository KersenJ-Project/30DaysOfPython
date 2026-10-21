from functools import reduce
from countries import countries as ct


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1. Mettre chaque pays en majuscules
countries_upper = list(map(lambda country: country.upper(), countries))
print(countries_upper)


# 2. Mettre chaque nombre au carré
square_numbers = list(map(lambda number: number ** 2, numbers))
print(square_numbers)


# 3. Mettre chaque nom en majuscules
names_upper = list(map(lambda name: name.upper(), names))
print(names_upper)


# 4. Filtrer les pays contenant "land"
countries_with_land = list(filter(lambda country: "land" in country, countries))
print(countries_with_land)


# 5. Filtrer les pays ayant exactement six caractères
countries_with_6_characters = list(filter(lambda country: len(country) == 6, countries))
print(countries_with_6_characters)


# 6. Filtrer les pays ayant six caractères ou plus
countries_with_6_or_more_characters = list(filter(lambda country: len(country) >= 6, countries))
print(countries_with_6_or_more_characters)


# 7. Filtrer les pays commençant par E
countries_start_with_E = list(filter(lambda country: country.startswith('E'), countries))
print(countries_start_with_E)


# 8. Enchaîner map, filter et reduce
result = reduce(
    lambda x, y: x + y,
    filter(
        lambda number: number % 2 == 0,
        map(lambda number: number ** 2, numbers)
    )
)
print(result)


# 9. Retourner uniquement les chaînes de caractères
def get_string_lists(lst):
    result = []

    for element in lst:
        if isinstance(element, str):
            result.append(element)

    return result


print(get_string_lists(["a", "asda", True, 1231, "dasda"]))


# 10. Additionner tous les nombres avec reduce
total_numbers = reduce(lambda x, y: x + y, numbers)
print(total_numbers)


# 11. Concaténer les noms français des pays
countries_fr = ['Estonie', 'Finlande', 'Suède', 'Danemark', 'Norvège', 'Islande']

phrase = reduce(
    lambda x, y: x + (", " if y != countries_fr[-1] else " et ") + y,
    countries_fr
)

print(f"{phrase} sont des pays d'Europe du Nord.")


# 12. Retourner les pays contenant un motif commun
def categorize_countries(pattern):
    result = []

    for country in ct:
        if pattern.lower() in country.lower():
            result.append(country)

    return result


print(categorize_countries('land'))
print(categorize_countries('ia'))
print(categorize_countries('island'))
print(categorize_countries('stan'))


# 13. Compter le nombre de pays par lettre initiale
def count_countries_by_first_letter():
    result = {}

    for country in ct:
        first_letter = country[0].upper()

        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1

    return result


print(count_countries_by_first_letter())


# 14. Retourner les dix premiers pays
def get_first_ten_countries():
    return ct[:10]


print(get_first_ten_countries())


# 15. Retourner les dix derniers pays
def get_last_ten_countries():
    return ct[-10:]


print(get_last_ten_countries())