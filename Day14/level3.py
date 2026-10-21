from functools import reduce
from countries_data import countries_data


# 1. Trier les pays par nom
countries_by_name = sorted(countries_data, key=lambda country: country["name"])

print("Pays triés par nom :")
for country in countries_by_name:
    print(country["name"])


# Trier les pays par capitale
countries_by_capital = sorted(countries_data, key=lambda country: country["capital"])

print("\nPays triés par capitale :")
for country in countries_by_capital:
    print(country["capital"], "-", country["name"])


# Trier les pays par population, du plus petit au plus grand
countries_by_population = sorted(countries_data, key=lambda country: country["population"])

print("\nPays triés par population :")
for country in countries_by_population:
    print(country["name"], "-", country["population"])


# 2. Trouver les dix langues présentes dans le plus de pays
languages = {}

for country in countries_data:
    for language in country["languages"]:
        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1

languages_sorted = sorted(
    languages.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nLes dix langues présentes dans le plus de pays :")
for language in languages_sorted[:10]:
    print(language[0], "-", language[1], "pays")


# 3. Trouver les dix pays les plus peuplés
most_populated_countries = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True
)

print("\nLes dix pays les plus peuplés :")
for country in most_populated_countries[:10]:
    print(country["name"], "-", country["population"])
