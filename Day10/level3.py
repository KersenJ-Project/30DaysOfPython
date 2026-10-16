from countries import countries
from countries_data import countries_data

for country in countries:
    if("land" in country):
        print(country)

fruits_list = ['banana', 'orange', 'mango', 'lemon']
inverse_fruits_list = []
for i in range(len(fruits_list)):
    inverse_fruits_list.append(fruits_list[-(i + 1)])

print(inverse_fruits_list)

language_seen = {}
for country in countries_data:
    for language in country["languages"]:
        if language in language_seen:
            language_seen[language] += 1
        else:
            language_seen[language] = 1

print(f"Nombre total de langues differentes : {len(language_seen)}")

top_10_language = sorted(
    language_seen.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]

for language, count in top_10_language:
    print(language, count)

top_10_countries_population = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True
)[:10]

for country in top_10_countries_population:
    print(country["name"], country["population"])