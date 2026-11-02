import re
import os
import sys
import csv

with open('./data/email_exchanges_big.txt', encoding="utf-8") as file:
    text = file.read()

    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        text
    )

print(emails)


def find_most_common_words(source, number):

    if os.path.isfile(source):
        with open(source, encoding="utf-8") as file:
            text = file.read()
    else:
        text = source

    words = re.findall(r"[a-zA-Z']+", text.lower())

    words_count = {}

    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    sorted_words = sorted(
        words_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return [
        (count, word)
        for word, count in sorted_words[:number]
    ]


print(find_most_common_words('./data/email_exchanges_big.txt', 10))
print(find_most_common_words('./data/email_exchanges_big.txt', 5))

print("Obama Speech:")
print(find_most_common_words('./data/obama_speech.txt', 10))

print("\nMichelle Obama Speech:")
print(find_most_common_words('./data/michelle_obama_speech.txt', 10))

print("\nDonald Trump Speech:")
print(find_most_common_words('./data/donald_speech.txt', 10))

print("\nMelina Trump Speech:")
print(find_most_common_words('./data/melina_trump_speech.txt', 10))


sys.path.append('./data')

from stop_words import stop_words

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-z\s]', '', text)

    return text

text = "Hello World! Python is GREAT. 123"

print(clean_text(text))

def remove_support_words(text):

    words = text.split()

    filtered_words = []

    for word in words:
        if word not in stop_words:
            filtered_words.append(word)

    return filtered_words

text = "the python language is very interesting"

print(remove_support_words(text))

def check_text_similarity(text1, text2):

    with open(text1) as f:
        content1 = f.read()

    with open(text2) as f:
        content2 = f.read()

    content1 = clean_text(content1)
    content2 = clean_text(content2)

    words_in_text1 = remove_support_words(content1)
    words_in_text2 = remove_support_words(content2)

    set1 = set(words_in_text1)
    set2 = set(words_in_text2)

    commond_words = set1.intersection(set2)
    all_words = set1.union(set2)

    similarity = (len(commond_words) / len(all_words)) * 100

    return similarity

similarity = check_text_similarity(
    './data/michelle_obama_speech.txt',
    './data/melina_trump_speech.txt'
)

print(f"Similarité : {similarity:.2f}%")

print("\nRomeo and Juliet:")
print(find_most_common_words('./data/romeo_and_juliet.txt', 10))


number_of_python = 0

with open('./data/hacker_news.csv', encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        title = row["title"]

        if "python" in title.lower():
            number_of_python += 1

print("Nombre de publications contenant Python :", number_of_python)


number_of_javascript = 0

with open('./data/hacker_news.csv', encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        title = row["title"]

        if "javascript" in title.lower():
            number_of_javascript += 1

print("Nombre de publications contenant JavaScript :", number_of_javascript)


number_of_java = 0

with open('./data/hacker_news.csv', encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        title = row["title"]

        if "java" in title.lower() and "javascript" not in title.lower():
            number_of_java += 1

print("Nombre de publications contenant Java :", number_of_java)