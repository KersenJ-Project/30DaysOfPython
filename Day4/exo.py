# Day 4

# 1. Concaténez les chaînes 'Thirty', 'Days', 'Of', 'Python'
result = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print("1.", result)

# 2. Concaténez 'Coding', 'For', 'All'
result = 'Coding' + ' ' + 'For' + ' ' + 'All'
print("2.", result)

# 3. Déclarez la variable company
company = "Coding For All"

# 4. Affichez company
print("4.", company)

# 5. Affichez la longueur de company
print("5.", len(company))

# 6. Convertissez company en majuscules
print("6.", company.upper())

# 7. Convertissez company en minuscules
print("7.", company.lower())

# 8. Utilisez capitalize(), title() et swapcase()
print("8. capitalize():", company.capitalize())
print("   title():", company.title())
print("   swapcase():", company.swapcase())

# 9. Découpez le premier mot de company
first_word = company[:6]
print("9.", first_word)

# 10. Vérifiez si company contient le mot Coding
print("10. index():", company.index("Coding"))
print("   find():", company.find("Coding"))
print("   in:", "Coding" in company)

# 11. Remplacez 'Coding' par 'Python'
print("11.", company.replace("Coding", "Python"))

# 12. Changez "Python for Everyone" en "Python for All"
sentence = "Python for Everyone"
print("12.", sentence.replace("Everyone", "All"))

# 13. Découpez company avec l'espace comme séparateur
print("13.", company.split(" "))

# 14. Découpez la liste de compagnies au niveau de la virgule
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("14.", companies.split(", "))

# 15. Caractère à l'indice 0
print("15.", company[0])

# 16. Dernier indice de company
print("16.", len(company) - 1)

# 17. Caractère à l'indice 10
print("17.", company[10])

# 18. Acronyme de 'Python For Everyone'
python_for_everyone = "Python For Everyone"
acronym = "".join(word[0] for word in python_for_everyone.split())
print("18.", acronym)

# 19. Acronyme de 'Coding For All'
coding_for_all = "Coding For All"
acronym = "".join(word[0] for word in coding_for_all.split())
print("19.", acronym)

# 20. Position de la première occurrence de C
print("20.", company.index("C"))

# 21. Position de la première occurrence de F
print("21.", company.index("F"))

# 22. Dernière occurrence de l dans 'Coding For All People'
text = "Coding For All People"
print("22.", text.rfind("l"))

# 23. Première occurrence de 'because'
sentence = (
    "You cannot end a sentence with because because because "
    "is a conjunction"
)
print("23.", sentence.find("because"))

# 24. Dernière occurrence de 'because'
print("24.", sentence.rindex("because"))

# 25. Extraire 'because because because'
start = sentence.find("because")
end = sentence.find("is a conjunction")
print("25.", sentence[start:end].strip())

# 26. Position de la première occurrence de 'because'
print("26.", sentence.find("because"))

# 27. Extraire 'because because because'
start = sentence.find("because")
end = sentence.find("is a conjunction")
print("27.", sentence[start:end].strip())

# 28. Est-ce que company commence par 'Coding' ?
print("28.", company.startswith("Coding"))

# 29. Est-ce que company se termine par 'coding' ?
print("29.", company.endswith("coding"))

# 30. Supprimer les espaces de début et de fin
text = "  Coding For All    "
print("30.", text.strip())


# 31. Vérifier isidentifier()
name1 = "30DaysOfPython"
name2 = "thirty_days_of_python"

print("31. 30DaysOfPython:", name1.isidentifier())
print("    thirty_days_of_python:", name2.isidentifier())


# 32. Joindre la liste avec '# '
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("32.", "# ".join(libraries))


# 33. Utiliser \n pour séparer les phrases
print("33.")
print("I am enjoying this challenge.\nI just wonder what is next.")


# 34. Utiliser \t pour créer des colonnes
print("34.")
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


# 35. Formatage de chaînes
radius = 10
area = 3.14 * radius ** 2

print("35.")
print(
    "The area of a circle with radius {} is {} meters square.".format(
        radius, area
    )
)

# 36. Formatage de chaînes avec les opérations
num_one = 8
num_two = 6

print("36.")
print("{} + {} = {}".format(num_one, num_two, num_one + num_two))
print("{} - {} = {}".format(num_one, num_two, num_one - num_two))
print("{} * {} = {}".format(num_one, num_two, num_one * num_two))
print("{} / {} = {:.2f}".format(num_one, num_two, num_one / num_two))
print("{} % {} = {}".format(num_one, num_two, num_one % num_two))
print("{} // {} = {}".format(num_one, num_two, num_one // num_two))
print("{} ** {} = {}".format(num_one, num_two, num_one ** num_two))