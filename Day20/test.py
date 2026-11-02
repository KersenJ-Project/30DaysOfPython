import webbrowser # module navigateur web pour ouvrir des sites

# liste d'urls : python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# ouvre la liste de sites ci-dessus dans un onglet différent
for url in url_lists:
    webbrowser.open_new_tab(url)