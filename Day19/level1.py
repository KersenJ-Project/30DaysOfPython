import json

with open('./data/obama_speech.txt') as f:
    lines = f.read().splitlines()
    number_of_lines = len(lines)
    number_of_words = 0
    for line in lines:
        words = line.split()
        number_of_words += len(words)
    print('Nombre de lignes :', number_of_lines)
    print('Nombre de mots total :', number_of_words)

with open('./data/michelle_obama_speech.txt') as f:
    lines = f.read().splitlines()
    number_of_lines = len(lines)
    number_of_words = 0
    for line in lines:
        words = line.split()
        number_of_words += len(words)
    print('Nombre de lignes :', number_of_lines)
    print('Nombre de mots total :', number_of_words)

with open('./data/donald_speech.txt') as f:
    lines = f.read().splitlines()
    number_of_lines = len(lines)
    number_of_words = 0
    for line in lines:
        words = line.split()
        number_of_words += len(words)
    print('Nombre de lignes :', number_of_lines)
    print('Nombre de mots total :', number_of_words)

with open('./data/melina_trump_speech.txt') as f:
    lines = f.read().splitlines()
    number_of_lines = len(lines)
    number_of_words = 0

    for line in lines:
        words = line.split()
        number_of_words += len(words)
    print('Nombre de lignes :', number_of_lines)
    print('Nombre de mots total :', number_of_words)


def most_spoken_languages(filename, number):
    with open(filename, encoding="utf-8") as file:
        countries = json.load(file)

        languages = {}

        for country in countries:
            for language in country["languages"]:
                if language in languages:
                    languages[language] += 1
                else:
                    languages[language] = 1

        sorted_countries =  sorted(
            languages.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [
            (count, language)
            for language, count in sorted_countries[:number]
        ]

print(most_spoken_languages('./data/countries_data.json', 10))
print(most_spoken_languages('./data/countries_data.json', 3))


def most_populated_countries(filename, number):
    with open(filename, encoding="utf-8") as file:
        countries = json.load(file)

        population_countries = []

        for country in countries:
            result = {
                "country": country["name"],
                "population": country["population"]
            }

            population_countries.append(result)

    sorted_countries = sorted(
        population_countries,
        key=lambda item: item["population"],
        reverse=True
    )

    return sorted_countries[:number]


print(most_populated_countries('./data/countries_data.json', 10))
print(most_populated_countries('./data/countries_data.json', 3))