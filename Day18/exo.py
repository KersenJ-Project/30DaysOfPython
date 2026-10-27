import re

paragraph = """I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."""

# Extraire les mots
words = re.findall(r"\b\w+\b", paragraph)

# Compter les occurrences de chaque mot
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Trier les mots par fréquence décroissante
sorted_words = sorted(
    word_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

# Afficher les fréquences sous la forme (nombre, mot)
result = [(count, word) for word, count in sorted_words]

print(result)


text = "Les positions sont -12, -4, -3, -1, 0, 4 et 8."

# Extraire les nombres, y compris les nombres négatifs
points = re.findall(r"-?\d+", text)

# Convertir les chaînes en entiers
points = [int(point) for point in points]

# Calculer la distance entre les deux positions extrêmes
distance = max(points) - min(points)

print("Points :", points)
print("Distance :", distance)


def is_valid_variable(name):
    pattern = r"[A-Za-z_][A-Za-z0-9_]*"

    # Vérifier la syntaxe du nom
    if not re.fullmatch(pattern, name):
        return False

    # Vérifier les mots réservés les plus courants
    reserved_words = [
        "False", "None", "True", "and", "as", "assert",
        "async", "await", "break", "class", "continue",
        "def", "del", "elif", "else", "except", "finally",
        "for", "from", "global", "if", "import", "in",
        "is", "lambda", "nonlocal", "not", "or", "pass",
        "raise", "return", "try", "while", "with", "yield"
    ]

    if name in reserved_words:
        return False

    return True


print(is_valid_variable("first_name"))   # True
print(is_valid_variable("first-name"))   # False
print(is_valid_variable("1first_name"))  # False
print(is_valid_variable("firstname"))    # True
print(is_valid_variable("class"))        # False



sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""


def clean_text(text):
    # Supprimer les caractères spéciaux
    cleaned = re.sub(r"[^A-Za-z\s]", "", text)

    # Remplacer les espaces multiples par un seul espace
    cleaned = re.sub(r"\s+", " ", cleaned)

    return cleaned.strip()


def most_frequent_words(text):
    # Extraire les mots
    words = re.findall(r"\b[A-Za-z]+\b", text)

    # Compter les occurrences sans Counter
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Trier par fréquence décroissante
    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Retourner les trois premiers sous la forme (nombre, mot)
    return [(count, word) for word, count in sorted_words[:3]]


cleaned_sentence = clean_text(sentence)

print(cleaned_sentence)
print(most_frequent_words(cleaned_sentence))