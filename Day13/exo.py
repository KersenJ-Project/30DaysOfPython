# Exo 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative__and_zero = [n for n in numbers if n <= 0]

print(negative__and_zero)

# Exo 2

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

# Exo 3

result = [
    (n, 1 , n , n**2, n**3, n**4, n**5)
    for n in range(11)
]

print(result)

# Exo 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [
    [country.upper(), country[:3].upper(), city.upper()]
    for item in countries
    for country, city in [item[0]]
]

print(result)

# Exo 5

result = [
    {'country': country.upper(), 'city': city.upper()}
    for item in countries
    for country, city in item[0]
]

print(result)

# Exo 6

names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')]
]

result = [
    first_name + ' ' + last_name
    for item in names
    for first_name, last_name in item[0]
]

print(result)

# Exo 7

# Calculer la pente à partir de deux points
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

print(slope(1, 2, 3, 6))