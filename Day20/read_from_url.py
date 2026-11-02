import requests

url = 'https://restcountries.eu/rest/v2/all'

response = requests.get(url)

print(response.status_code)

if response.status_code == 200:
    countries = response.json()
    print(countries)
else:
    print("Erreur lors de la récupération des données.")
    print(response.text)