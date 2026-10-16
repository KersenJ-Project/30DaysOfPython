import math
import cmath


def add_two_numbers(a, b):
    return a + b


def area_of_circle(r):
    return math.pi * r * r


def add_all_nums(*args):
    if not all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in args):
        return "Erreur : tous les arguments doivent être numériques."
    return sum(args)


def convert_celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def check_season(month):
    month = month.strip().lower()
    seasons = {
        "hiver": ["décembre", "decembre", "janvier", "février", "fevrier"],
        "printemps": ["mars", "avril", "mai"],
        "été": ["juin", "juillet", "août", "aout"],
        "automne": ["septembre", "octobre", "novembre"],
    }
    for season, months in seasons.items():
        if month in months:
            return season.capitalize()
    return "Mois invalide"


def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        raise ValueError("La pente est indéfinie lorsque x1 et x2 sont égaux.")
    return (y2 - y1) / (x2 - x1)


def solve_quadratic_eqn(a, b, c):
    if a == 0:
        if b == 0:
            return "Aucune solution unique." if c != 0 else "Infinité de solutions."
        return (-c / b,)
    discriminant = b * b - 4 * a * c
    racine = cmath.sqrt(discriminant)
    return ((-b + racine) / (2 * a), (-b - racine) / (2 * a))


def print_list(items):
    for item in items:
        print(item)


def reverse_list(items):
    reversed_items = []
    for index in range(len(items) - 1, -1, -1):
        reversed_items.append(items[index])
    return reversed_items


def capitalize_list_items(items):
    return [item.upper() if isinstance(item, str) else item for item in items]


def add_item(items, item):
    result = items.copy()
    result.append(item)
    return result


def remove_item(items, item):
    result = items.copy()
    if item in result:
        result.remove(item)
    return result


def sum_of_numbers(number):
    return sum(range(1, number + 1))


def sum_of_odds(number):
    return sum(value for value in range(1, number + 1) if value % 2 != 0)


def sum_of_even(number):
    return sum(value for value in range(1, number + 1) if value % 2 == 0)
