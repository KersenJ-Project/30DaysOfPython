import keyword
import math


def is_prime(number):
    if not isinstance(number, int) or isinstance(number, bool) or number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, math.isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def all_unique(items):
    for index, item in enumerate(items):
        if item in items[index + 1:]:
            return False
    return True


def all_same_type(items):
    if not items:
        return True
    first_type = type(items[0])
    return all(type(item) is first_type for item in items)


def is_valid_variable(name):
    return isinstance(name, str) and name.isidentifier() and not keyword.iskeyword(name)


def most_spoken_languages(countries_data, limit=10):
    language_counts = {}
    for country in countries_data:
        for language in country.get("languages", []):
            language_counts[language] = language_counts.get(language, 0) + 1
    return sorted(language_counts.items(), key=lambda item: item[1], reverse=True)[:limit]


def most_populated_countries(countries_data, limit=10):
    return sorted(
        countries_data,
        key=lambda country: country.get("population", 0),
        reverse=True
    )[:limit]
