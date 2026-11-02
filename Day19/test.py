import os
import json
import csv
import xml.etree.ElementTree as ET

with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')


# os.remove('./files/example.txt')

# JSON
personne_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# convertissons JSON en dictionnaire
personne_dct = json.loads(personne_json)
print(type(personne_dct))
print(personne_dct)
print(personne_dct['name'])


# dictionnaire python
personne = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# convertissons-le en json
personne_json = json.dumps(personne, indent=4) # indent peut être 2, 4, 8. Il embellit le json
print(type(personne_json))
print(personne_json)

with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(personne, f, ensure_ascii=False, indent=4)


with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # nous utilisons la méthode reader pour lire le csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Noms des colonnes : {", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} est un enseignant. Il vit à {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Nombre de lignes : {line_count}')


tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Balise racine :', root.tag)
print('Attribut :', root.attrib)
for child in root:
    print('champ : ', child.tag)
