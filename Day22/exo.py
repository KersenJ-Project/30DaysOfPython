
import requests
from bs4 import BeautifulSoup
import json

# 1. Récupérer le contenu du site
url = "https://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")

# 2. Créer notre dictionnaire principal
data = {
    "title": soup.title.get_text(strip=True),
    "url": url,
    "sections": {}
}

# 3. Extraire les statistiques présentées sous forme de cartes
stat_lists = soup.select(".content-area .bu-stat-list")

for stat_list in stat_lists:

    # Trouver le titre de la catégorie
    heading = stat_list.find_previous(
        "h4", class_="stat-group-title"
    )

    category = heading.get_text(strip=True)

    # Dictionnaire contenant les statistiques de cette catégorie
    stats = {}

    # Parcourir toutes les cartes
    cards = stat_list.select(".bu-stat-single")

    for card in cards:

        label = card.select_one(".bu-stat-title")
        value = card.select_one(".bu-stat-value-container")

        if label and value:
            label = label.get_text(strip=True)
            value = value.get_text(strip=True)

            stats[label] = value

    data["sections"][category] = stats


# 4. Extraire les statistiques présentées sous forme de listes
stat_sections = soup.select(
    ".facts-stats-content section.stat-section"
)

for section in stat_sections:

    heading = section.find(
        "h4", class_="stat-group-title"
    )

    category = heading.get_text(strip=True)

    stats = {}

    items = section.select(".custom-stat-list li")

    for item in items:

        label = item.select_one(".stat-label")
        value = item.select_one(".stat-figure")

        if label and value:
            label = label.get_text(strip=True)
            value = value.get_text(strip=True)

            stats[label] = value

    data["sections"][category] = stats


# 5. Sauvegarder les données dans un fichier JSON
with open("./data/bu_facts.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Données sauvegardées avec succès !")